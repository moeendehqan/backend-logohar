import json
from Authentication import admin_getinfouser
import config
import function
from hazm import *
import datetime


def admin_setpallet(data):
    user = json.loads(admin_getinfouser(data))
    if user['reply'] == False: return admin_getinfouser(data)
    user = user['infouser']
    pallet = data['pallet']
    normalizer = Normalizer()
    sent2vec_model = SentEmbedding('models/sent2vec-naab.model')
    if len(pallet['id']) == 0:
        pallet['id_creator'] = data['id']
        checkColor = config.db['pallet'].find_one({'firstColor':pallet['firstColor'],'secondColor':pallet['secondColor'],'thirdColor':pallet['thirdColor']})
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
        config.db['palletBank'].insert_one(pallet)
        return json.dumps({'reply':True})
    else:
        return json.dumps({'reply':True})
