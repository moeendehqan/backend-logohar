from flask_restful import Resource, reqparse, request
from app.service.validation_servise import  validation_service
from app.service.nlp_service import sent_vector


creator_parser = reqparse.RequestParser()
creator_parser.add_argument('lang', type=str, help='زبان انتخاب نشده',required=True)
creator_parser.add_argument('dispalyName', type=str, help='نام را وارد کنید',required=True)
creator_parser.add_argument('persianName', type=str, help='نام را وارد کنید',required=False)
creator_parser.add_argument('keywords',action='append',type=str, required=True, help='کلیدواژه انتخاب نشده')
creator_parser.add_argument('jobs',action='append',type=str, required=True, help='دسته بندی انتخاب نشده')
creator_parser.add_argument('classLogo',action='append',type=str, required=True, help='نوع لوگو انتخاب نشده')
creator_parser.add_argument('pallet',type=str, required=True, help='پالت انتخاب نشده')


class creator_resource(Resource):
    def post(self):
        args = creator_parser.parse_args()
        obj_valid = validation_service()
        name_valid = obj_valid.BusinessName(args['lang'], args['dispalyName'], args['persianName'])
        if name_valid[1] != 200:
            return name_valid
        list_validation = [obj_valid.contains_only_persian(i) for i in args['keywords']]
        if False in list_validation:
            return {'result':False,'message':'کلید واژه ها میبایست به فارسی باشد'},200
        object_sent_vector = sent_vector()
        
        if args['lang'] == 'persian':
            args['name_vector'] = object_sent_vector.word_normaloize_and_vector_list(args['dispalyName'])
        else:
            args['name_vector'] = object_sent_vector.word_normaloize_and_vector_list(args['persianName'])
        print(args)
        

        return True
