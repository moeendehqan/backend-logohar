from flask_restful import Resource, reqparse
from app.models.pallet_models import pallet
from app.exceptions.not_found_admin import admin_validator
from app.models.fact_color_type_models import fact_color_type
from app.models.fact_jobs_models import fact_jobs
from app.models.fact_class_models import fact_class
from app.service.nlp_service import sent_vector
import datetime

pallet_parser = reqparse.RequestParser()
pallet_parser.add_argument('id', type=str, help='کوکی ذخیر نشده، لطفا مجددا وارد شوید',required=True)

new_pallet_parser = reqparse.RequestParser()
new_pallet_parser.add_argument('id', type=str, required=True, help='کوکی ذخیر نشده، لطفا مجددا وارد شوید')
new_pallet_parser.add_argument('first_color', type=str, required=True, help='اولین رنگ وارد نشده')
new_pallet_parser.add_argument('secend_color', type=str, required=True, help='دومین رنگ وارد نشده')
new_pallet_parser.add_argument('third_color', type=str, required=True, help='سومین رنگ وارد نشده')
new_pallet_parser.add_argument('type_color', type=str, required=True, help='نوع رنگ وارد نشده')
new_pallet_parser.add_argument('jobs',action='append',  type=str, required=True, help='دسته بندی صنفی وارد نشده')
new_pallet_parser.add_argument('keywords', type=str, required=True, help='کلیدواژه وارد نشده')
new_pallet_parser.add_argument('logo_class',action='append',type=str, required=True, help='نوع لوگو وارد نشده')


del_pallet_parser = reqparse.RequestParser()
del_pallet_parser.add_argument('id', type=str, help='کوکی ذخیر نشده، لطفا مجددا وارد شوید',required=True)
del_pallet_parser.add_argument('id_pallet', type=str, help='پالتی برای حذف انتخاب نشده',required=True)



class pallet_tank_resource(Resource):
    def post(self):
        args = pallet_parser.parse_args()
        admin_validator(id=args['id']).admin_id_exists()
        pallet_tank = pallet.get_pallet_tank()
        return pallet_tank

class pallet_resource(Resource):
    def post(self):
        args = new_pallet_parser.parse_args()
        admin_validator(id=args['id']).admin_id_exists()
        type_color = fact_color_type.find_by_name(args['type_color'])
        jobs = [fact_jobs.find_by_name(x) for x in args['jobs']]
        logo_class = [fact_class.find_by_name(x) for x in args['logo_class']]
        print(logo_class)
        object_sent_vector = sent_vector()
        keywords = str(args['keywords']).split('-')
        keywords = [object_sent_vector.normalize_word(x) for x in keywords]
        keywords_vectors = [object_sent_vector.word_normaloize_and_vector_list(x) for x in keywords]
        new_pallet = pallet(
            first_color = args['first_color'],
            secend_color = args['secend_color'],
            third_color = args['third_color'],
            type_color = type_color['name'],
            type_color_name = type_color['title'],
            type_color_name_vector = type_color['vector'],
            jobs = [x['name'] for x in jobs],
            jobs_name = [x['title'] for x in jobs],
            jobs_name_vector = [x['vector'] for x in jobs],
            logo_class = [x['name'] for x in logo_class],
            logo_class_name = [x['title'] for x in logo_class],
            logo_class_name_vector = [x['vector'] for x in logo_class],
            keywords = keywords,
            keywords_vectors = keywords_vectors,
            creator = args['id'],
            create_date = datetime.datetime.now()
        )
        new_pallet.save()
        return True, 200
    def delete(self):
        args = del_pallet_parser.parse_args()
        admin_validator(id=args['id']).admin_id_exists()
        result = pallet.delete_pallet(args['id_pallet'])
        if result:
            return True, 200
        else:
            return {'message':'مورد یافت نشد برای حذف'},403



