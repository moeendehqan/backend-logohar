from flask_restful import Resource, reqparse, request
from app.service.validation_servise import validation_service

BusinessName_parser = reqparse.RequestParser()
BusinessName_parser.add_argument('lang', type=str, help='زبان انتخاب نشده است',required=True)
BusinessName_parser.add_argument('dispalyName', type=str, help='نام برند یافت نشد',required=True)
BusinessName_parser.add_argument('persianName', type=str, help='نام فارسی برند یافت نشد',required=True)

class BusinessName_resource(Resource):
    def post(self):
        args = BusinessName_parser.parse_args()
        objValidation =  validation_service()
        return objValidation.BusinessName(args['lang'],args['dispalyName'],args['persianName'])


