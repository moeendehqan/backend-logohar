from flask_restful import Resource, reqparse, request
from app.service.validation_servise import validation_service

BusinessName_parser = reqparse.RequestParser()
BusinessName_parser.add_argument('lang', type=str, help='زبان انتخاب نشده است',required=True)
BusinessName_parser.add_argument('dispalyName', type=str, help='نام برند یافت نشد',required=True)
BusinessName_parser.add_argument('persianName', type=str, help='نام فارسی برند یافت نشد',required=True)


Keywords_parser = reqparse.RequestParser()
Keywords_parser.add_argument('keywords',action='append',type=str, required=True, help='کلید واژه ها')

class BusinessName_resource(Resource):
    def post(self):
        args = BusinessName_parser.parse_args()
        objValidation =  validation_service()
        return objValidation.BusinessName(args['lang'],args['dispalyName'],args['persianName'])
    
class Keywords_resource(Resource):
    def post(self):
        args = Keywords_parser.parse_args()
        objValidation =  validation_service()
        list_validation = [objValidation.contains_only_persian(i) for i in args['keywords']]
        if False in list_validation:
            return {'result':False,'message':'کلید واژه ها میبایست به فارسی باشد'},200
        return {'result':True,'message':''},200
