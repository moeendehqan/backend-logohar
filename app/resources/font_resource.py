from flask_restful import Resource, reqparse, request
from app.exceptions.not_found_admin import admin_validator
from app.models.font_model import font
from app.models.fact_jobs_models import fact_jobs
from app.models.fact_class_models import fact_class
import os
import random

admin_parser = reqparse.RequestParser()
admin_parser.add_argument('id', type=str, help='کوکی ذخیر نشده، لطفا مجددا وارد شوید',required=True)



del_font_parser = reqparse.RequestParser()
del_font_parser.add_argument('id', type=str, help='کوکی ذخیر نشده، لطفا مجددا وارد شوید',required=True)
del_font_parser.add_argument('id_font', type=str, help='پالتی برای حذف انتخاب نشده',required=True)


class font_resource(Resource):
    def post(self):
        idd = request.form['id']
        admin_validator(id=idd).admin_id_exists()
        jobs = request.form['jobs'].split(',')
        if len(jobs) == 0:
            return {'message':'دستبندی شغلی خالی است'},403
        logo_class = request.form['logo_class'].split(',')
        if len(logo_class) == 0:
            return {'message':'نوع لوگو خالی است'},403
        jobs = [fact_jobs.find_by_name(x) for x in jobs]
        logo_class = [fact_class.find_by_name(x) for x in logo_class]
        file = request.files['file']
        file_type =  file.content_type
        file_name = file.filename
        weight = request.form['weight']
        name = request.form['name']
        public_folder = os.path.join(os.getcwd(), 'public')
        font_folder = os.path.join(public_folder,'fonts')
        existing_font = font.existing(name, weight)
        if existing_font:
            return {'message': 'تکراری است'}, 409
        if not os.path.exists(font_folder):
            os.makedirs(font_folder)
        file_name_system = str(random.randint(10000,99999))+'_'+file_name
        file_path = os.path.join(font_folder, file_name_system)
        new_font = font(
            name = name,
            jobs = [x['name'] for x in jobs],
            jobs_name = [x['title'] for x in jobs],
            jobs_name_vector = [x['vector'] for x in jobs],
            logo_class = [x['name'] for x in logo_class],
            logo_class_name = [x['title'] for x in logo_class],
            logo_class_name_vector = [x['vector'] for x in logo_class],
            file_type = file_type,
            file_name =file_name,
            file_name_system = file_name_system,
            weight = weight,
            file_path = font_folder,
            creator = idd,
        )

        file.save(file_path)
        new_font.save()
        return True,200
    def delete(self):
        args = del_font_parser.parse_args()
        admin_validator(id=args['id']).admin_id_exists()
        result = font.delete_font(args['id_font'])
        if result:
            return True, 200
        else:
            return {'message':'مورد یافت نشد برای حذف'},403
        
class font_tank_resource(Resource):
    def post(self):
        args = admin_parser.parse_args()
        admin_validator(args['id']).admin_id_exists()
        result = font.all()
        return result,200