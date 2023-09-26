import json
from Authentication import admin_getinfouser
import config
import function
from hazm import *



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
        pallet['typeColorName'] = function.findTitleTypeColor(pallet['typeColor'])
        if pallet['typeColorName'] == '':
            return json.dumps({'reply':False,'msg':'عنوام نوع پالت یافت نشد'})
        typeColorWordVector = normalizer.normalize(pallet['typeColorName'])
        pallet['typeColorWordVector'] = sent2vec_model[typeColorWordVector]

        print(pallet)
        return json.dumps({'reply':True})
    else:
        return json.dumps({'reply':True})
