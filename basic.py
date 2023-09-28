import json
from Authentication import admin_getinfouser
import config
import function
from hazm import *
import datetime
import pandas as pd


def admin_setpallet(data):
    user = json.loads(admin_getinfouser(data))
    if user['reply'] == False: return admin_getinfouser(data)
    user = user['infouser']
    pallet = data['pallet']
    normalizer = Normalizer()
    sent2vec_model = SentEmbedding('models/sent2vec-naab.model')
    if len(pallet['id']) == 0:
        del pallet['id']
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
        pallet['edith'] = False
        pallet['edithFrom'] = None
        pallet['idEdithor'] = None
        config.db['bankPallet'].insert_one(pallet)
        return json.dumps({'reply':True})
    else:
        return json.dumps({'reply':True})



def admin_getstaticspallet(data):
    user = json.loads(admin_getinfouser(data))
    if user['reply'] == False: return admin_getinfouser(data)
    dic = {}
    df = pd.DataFrame(config.db['bankPallet'].find({},{'_id':0,'typeColor':1,'typeJob':1,'idEdithor':1,'idCreator':1}))
    dic['create'] = len(df[df['idCreator']==data['id']])
    dic['edith'] = len(df[df['idEdithor']==data['id']])
    dic['typeColor'] = df['typeColor'].value_counts().to_dict()
    dic['typeJob'] = df['typeJob'].explode().value_counts().to_dict()
    return json.dumps({'reply':True,'dic':dic})


def admin_getbankpallet(data):
    user = json.loads(admin_getinfouser(data))
    if user['reply'] == False: return admin_getinfouser(data)
    df = pd.DataFrame(config.db['bankPallet'].find({'edith':False},{'typeColorWordVector':0,'typeJobWordVector':0,'keywordsWordVector':0}))
    df['_id'] = df['_id'].apply(str)
    df['createDate'] = df['createDate'].apply(function.dateToJalali)
    df['createDate'] = df['createDate'].apply(str)
    df = df.fillna(0)
    df = df.rename(columns={'_id':'id'})
    print(df)
    df = df.to_dict('records')
    return json.dumps({'reply':True,'df':df})