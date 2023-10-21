
import config
from persiantools.jdatetime import JalaliDate
import hashlib
from hazm import *
import xml.etree.ElementTree as ET

from pymongo import MongoClient
client = MongoClient()
db = client['logohar']


def findTitleTypeColor(name):
    title = ''
    for i in config.categoryColor:
        if i['name'] == name:
            title = i['title']
            break
    return title
    

def findTitleTypeJob(nameList):
    titleList = []
    for j in nameList:
        for i in config.categoryJob:
            if i['name'] == j:
                titleList.append(i['title'])
                break
    return titleList
    

def dateToJalali(date):
    return JalaliDate.to_jalali(date)



def listToStrByDash(lst):
    result =''
    for l in lst:
        result = result +' ' + l + ' - '
    return result


def hash_file_content(file_content):
    # ایجاد هش MD5 برای محتوای فایل
    md5_hash = hashlib.md5()
    md5_hash.update(file_content)
    return md5_hash.hexdigest()

def is_duplicate_content(file_content):
    existing_files = config.fs.find()
    for existing_file in existing_files:
        existing_content = existing_file.read()
        if existing_content == file_content:
            return True
    return False




class Vectorize:
    def __init__(self):
        self.normalizer = Normalizer()
        self.sent2vec_model = SentEmbedding(r'D:\New folder (3)\projetct\logohar\backend\app\service\nlp_file_models\sent2vec-naab.model')
    
    def normalize_word(self,word):
        return self.normalizer.normalize(word)

    def str_to_vector_list(self,word):
        return self.sent2vec_model[word].tolist()



def get_svg_size(svg_content):
    try:
        root = ET.fromstring(svg_content)
        width = root.attrib.get('width')
        height = root.attrib.get('height')
        return {'width': width, 'height': height}
    except ET.ParseError as e:
        print(f'Error parsing SVG: {e}')
        return None
    


ob = Vectorize()


df = db['fact_category'].find({})
for i in df:
    norm = ob.normalize_word(i['title'])
    vctr = ob.str_to_vector_list(norm)
    db['fact_category'].update_one({'_id':i['_id']},{'$set':{'title':norm,'vector':vctr}})
    print(i)