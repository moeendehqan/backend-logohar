import json
from Authentication import admin_getinfouser
import config
import function
from hazm import *
import datetime
import pandas as pd
from bson import ObjectId
import base64
from io import BytesIO
import random
from flask import jsonify

import base64


def admin_setpallet(data):
    user = json.loads(admin_getinfouser(data))
    if user['reply'] == False: return admin_getinfouser(data)
    user = user['infouser']
    pallet = data['pallet']
    normalizer = Normalizer()
    sent2vec_model = SentEmbedding('models/sent2vec-naab.model')
    pallet['idCreator'] = data['id']
    checkColor = config.db['bankPallet'].find_one({'firstColor':pallet['firstColor'],'secondColor':pallet['secondColor'],'thirdColor':pallet['thirdColor']})
    if checkColor !=None :
        return json.dumps({'reply':False,'msg':'هر سه رنگ قبلا در پایگاه داده ثبت شده'})
    if len(pallet['typeJob']) == 0:
        return json.dumps({'reply':False,'msg':'حداقل یک رشته صنفی باید وارد شده باشد'})
    if len(pallet['keywords']) == 0:
        return json.dumps({'reply':False,'msg':'کلیدواژه کمتر از یک واحد است'})
    pallet['typeColorName'] = function.findTitleTypeColor(pallet['typeColor'])
    if pallet['typeColorName'] == '':
        return json.dumps({'reply':False,'msg':'عنوان نوع پالت یافت نشد'})
    typeColorWordVector = normalizer.normalize(pallet['typeColorName'])
    pallet['typeColorWordVector'] = sent2vec_model[typeColorWordVector].tolist()
    pallet['typeJobName'] = function.findTitleTypeJob(pallet['typeJob'])
    pallet['typeJobWordVector'] = [sent2vec_model[normalizer.normalize(x)].tolist() for x in pallet['typeJobName']]
    pallet['keywords'] = pallet['keywords'].split('-')
    pallet['keywords'] = [normalizer.normalize(x) for x in pallet['keywords']]
    pallet['keywordsWordVector'] = [sent2vec_model[x].tolist() for x in pallet['keywords']]
    pallet['createDate'] = datetime.datetime.now()
    config.db['bankPallet'].insert_one(pallet)
    return json.dumps({'reply':True})


def admin_getstaticspallet(data):
    user = json.loads(admin_getinfouser(data))
    if user['reply'] == False: return admin_getinfouser(data)
    dic = {}
    df = pd.DataFrame(config.db['bankPallet'].find({},{'_id':0,'typeColor':1,'typeJob':1,'idEdithor':1,'idCreator':1}))
    if len(df)==0:
        return json.dumps({'reply':False})
    dic['create'] = len(df[df['idCreator']==data['id']])
    dic['typeColor'] = df['typeColor'].value_counts().to_dict()
    dic['typeJob'] = df['typeJob'].explode().value_counts().to_dict()
    return json.dumps(dic)


def admin_getbankpallet(data):
    user = json.loads(admin_getinfouser(data))
    if user['reply'] == False: return admin_getinfouser(data)
    df = pd.DataFrame(config.db['bankPallet'].find({},{'typeColorWordVector':0,'typeJobWordVector':0,'keywordsWordVector':0}))
    if len(df)>0:
        df['_id'] = df['_id'].apply(str)
        df['createDate'] = df['createDate'].apply(function.dateToJalali)
        df['createDate'] = df['createDate'].apply(str)
        df['keywords'] = df['keywords'].apply(function.listToStrByDash)
        df = df.fillna(0)
        df = df.rename(columns={'_id':'id'})
        df = df.to_dict('records')
        return json.dumps({'reply':True,'df':df})
    return json.dumps({'reply':False})


def admin_setvector(id, idVector, fileVector, typeJobVector, keywords):
    file_content = fileVector.read()
    svg_size = function.get_svg_size(file_content)
    if not svg_size:
        return json.dumps({'reply':False})
    width = int(svg_size['width'][:-2])
    height = int(svg_size['height'][:-2])
    aspect_ratio = width / height
    filename = fileVector.filename
    vecrtorize = function.Vectorize()
    if function.is_duplicate_content(file_content):
        return json.dumps({'reply': False,'msg':'وکتور تکراری است. قبلا ثبت شده.'})
    nameFileSystem = str(random.randint(1000000000,9999999999))+'.svg'
    keywords = keywords.split('-')
    keywords = [vecrtorize.normalize_word(x) for x in keywords]
    keywordsWordVector = [vecrtorize.str_to_vector_list(x) for x in keywords]
    typeJob = typeJobVector.split(',')
    typeJobName = function.findTitleTypeJob(typeJob)
    typeJobNameVector = [vecrtorize.normalize_word(x) for x in typeJobName]
    typeJobNameVector = [vecrtorize.str_to_vector_list(x) for x in typeJobNameVector]
    createDate = datetime.datetime.now()
    config.fs.put(file_content, filename = filename, nameFileSystem=nameFileSystem, createDate = createDate, content_type = 'image/svg+xml',
                  keywords=keywords, keywordsWordVector=keywordsWordVector, typeJob = typeJob, typeJobName = typeJobName,
                  typeJobVector = typeJobNameVector, idCreator = id, width = width, height = height, aspect_ratio = aspect_ratio
                  )
    return json.dumps({'reply':True})


def admin_getvectorbank(data):
    user = json.loads(admin_getinfouser(data))
    if user['reply'] == False: return admin_getinfouser(data)
    df = config.fs.find()
    dff = []
    for file_object in df:
        dic = {
            'file': base64.b64encode(file_object.read()).decode('utf-8'),
            'filename':file_object.filename,
            'nameFileSystem':file_object.nameFileSystem,
            'createDate':str(function.dateToJalali(file_object.createDate)),
            'content_type':file_object.content_type,
            'keywords':file_object.keywords,
            'typeJob':file_object.typeJob,
            'typeJobName':file_object.typeJobName,
            'aspect_ratio':'1:'+str(int(file_object.aspect_ratio)),
        }
        dff.append(dic)
    return json.dumps({'reply':True,'df':dff})


def admin_setfont(id, font_id, file, typeJob, weight, name):
    check = config.db['font'].find_one({'name':name,'weight':weight})
    if check != None:
        return json.dumps({'reply':False,'msg':'ثبت نشد. فونت با این نام و وزن قبلا ثبت شده'}) 
    file_name = file.filename
    file_system_name = str(random.randint(1000000,9999999))+"_"+file_name
    vecrtorize = function.Vectorize()
    typeJob = typeJob.split(',')
    typeJobName = function.findTitleTypeJob(typeJob)
    typeJobNameVector = [vecrtorize.normalize_word(x) for x in typeJobName]
    typeJobNameVector = [vecrtorize.str_to_vector_list(x) for x in typeJobNameVector]
    createDate = datetime.datetime.now()
    file.save(f"public/fonts/{file_system_name}")
    config.db['font'].insert_one({'file_name':file_name, 'name':name, 'file_system_name':file_system_name, 'typeJob':typeJob, 'typeJobName':typeJobName, 'typeJobNameVector':typeJobNameVector,'creatorId':id, 'weight':weight,'createDate':createDate})
    return json.dumps({'reply':True})


def admin_getfontsname(data):
    user = json.loads(admin_getinfouser(data))
    if user['reply'] == False: return admin_getinfouser(data)
    df = config.db['font'].distinct('name')
    return json.dumps({'reply':True,'fonts_name':df})

def admin_getfontsbank(data):
    user = json.loads(admin_getinfouser(data))
    if user['reply'] == False: return admin_getinfouser(data)
    df = pd.DataFrame(config.db['font'].find({},{'typeJobNameVector':0}))
    if len(df) == 0:
        return json.dumps({'reply':True,'df':[]})
    df['_id'] = df['_id'].apply(str)
    df['createDate'] = df['createDate'].apply(function.dateToJalali)
    df['createDate'] = df['createDate'].apply(str)
    df = df.to_dict('records')
    return json.dumps({'reply':True,'df':df})
