from pymongo import MongoClient

client = MongoClient()
db = client['logohar']



categoryColor = [{'name':'warm','title':'گرم'},{'name':'cold','title':'سرد'},{'name':'fancy','title':'فانتزی'},{'name':'pastel','title':'پاستیلی'}]
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