
from hazm import *


from pymongo import MongoClient
client = MongoClient()
db = client['logohar']



categoryJob = [
    {'title':'گردشگری','name':'tourism'},
    {'title':'سرگرمی و ورزشی','name':'sports'},
    {'title':'فرهنگی و آموزشی','name':'educational'},
    {'title':'حیوانات خانگی و دام','name':'pet'},
    {'title':'کشاورزی و محیط زیست','name':'agriculture'},
    {'title':'آرایشی و بهداشتی','name':'cosmetics'},
    {'title':'املاک','name':'estate'},
    {'title':'وسایل نقلیه','name':'vehicles'},
    {'title':'پزشکی و سلامت','name':'health'},
    {'title':'تولید و صنعت','name':'industry'},
    {'title':'خوراکی و آشامیدنی','name':'food'},
    {'title':'فن آوری','name':'technology'},
    {'title':'مالی و اقتصادی','name':'financial'},
    {'title':'مذهبی','name':'religious'},
    {'title':'لوازم خانگی','name':'appliances'},
    {'title':'ابزار آلات','name':'tools'},
    {'title':'حقوقی و مشاوره','name':'legal'},
    {'title':'حمل و نقل و پست','name':'shipping'},
    {'title':'پوشاک و مد','name':'fashion'},
    {'title':'فنی مهندسی','name':'engineering'},
]

class Vectorize:
    def __init__(self):
        self.normalizer = Normalizer()
        self.sent2vec_model = SentEmbedding(r'D:\New folder (3)\projetct\logohar\backend\app\service\nlp_file_models\sent2vec-naab.model')
    
    def normalize_word(self,word):
        return self.normalizer.normalize(word)

    def str_to_vector_list(self,word):
        return self.sent2vec_model[word].tolist()




def init_fact_color_type():
    print('start init collection fact_color_type')
    ob = Vectorize()
    db['fact_color_type'].drop()
    lst = [
        {'name':'warm','title':'گرم','vector':[]},
        {'name':'cold','title':'سرد','vector':[]},
        {'name':'Fancy','title':'فانتزی','vector':[]},
        {'name':'complementary','title':'مکمل','vector':[]},
    ]
    for i in lst:
        norm = ob.normalize_word(i['title'])
        vctr = ob.str_to_vector_list(norm)
        db['fact_color_type'].insert_one({'title':norm,'vector':vctr,'name':i['name']})


def init_fact_jobs():
    print('start init collection fact_jobs')
    ob = Vectorize()
    db['fact_jobs'].drop()
    lst = [
        {'vector':[],'title':'گردشگری','name':'tourism'},
        {'vector':[],'title':'سرگرمی و ورزشی','name':'sports'},
        {'vector':[],'title':'فرهنگی و آموزشی','name':'educational'},
        {'vector':[],'title':'حیوانات خانگی و دام','name':'pet'},
        {'vector':[],'title':'کشاورزی و محیط زیست','name':'agriculture'},
        {'vector':[],'title':'آرایشی و بهداشتی','name':'cosmetics'},
        {'vector':[],'title':'املاک','name':'estate'},
        {'vector':[],'title':'وسایل نقلیه','name':'vehicles'},
        {'vector':[],'title':'پزشکی و سلامت','name':'health'},
        {'vector':[],'title':'تولید و صنعت','name':'industry'},
        {'vector':[],'title':'خوراکی و آشامیدنی','name':'food'},
        {'vector':[],'title':'فن آوری','name':'technology'},
        {'vector':[],'title':'مالی و اقتصادی','name':'financial'},
        {'vector':[],'title':'مذهبی','name':'religious'},
        {'vector':[],'title':'لوازم خانگی','name':'appliances'},
        {'vector':[],'title':'ابزار آلات','name':'tools'},
        {'vector':[],'title':'حقوقی و مشاوره','name':'legal'},
        {'vector':[],'title':'حمل و نقل و پست','name':'shipping'},
        {'vector':[],'title':'پوشاک و مد','name':'fashion'},
        {'vector':[],'title':'فنی مهندسی','name':'engineering'},
    ]
    for i in lst:
        norm = ob.normalize_word(i['title'])
        vctr = ob.str_to_vector_list(norm)
        db['fact_jobs'].insert_one({'title':norm,'vector':vctr,'name':i['name']})




def init_fact_class():
    print('start init collection fact_class')
    ob = Vectorize()
    db['fact_class'].drop()
    lst = [
        {'name':'modern','title':'مدرن','vector':[]},
        {'name':'classic','title':'کلاسیک','vector':[]},
        {'name':'fantasy','title':'فانتزی','vector':[]},
        {'name':'abstract','title':'انتزاعی','vector':[]},
    ]
    for i in lst:
        norm = ob.normalize_word(i['title'])
        vctr = ob.str_to_vector_list(norm)
        db['fact_class'].insert_one({'title':norm,'vector':vctr,'name':i['name']})
  

init_fact_color_type()
init_fact_jobs()
init_fact_class()