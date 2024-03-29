from flask_restful import Resource, reqparse, request
from app.exceptions.not_found_admin import admin_validator
from app.models.fact_jobs_models import fact_jobs
from app.models.fact_class_models import fact_class
from app.service.nlp_service import sent_vector
from app.models.vector_model import vector
from app.service.vector_service import vector_service
from io import BytesIO
from app.service.file_service import file_service

vector_tank_parser = reqparse.RequestParser()
vector_tank_parser.add_argument('id', type=str, help='کوکی ذخیر نشده، لطفا مجددا وارد شوید',required=True)

del_vector_parser = reqparse.RequestParser()
del_vector_parser.add_argument('id', type=str, help='کوکی ذخیر نشده، لطفا مجددا وارد شوید',required=True)
del_vector_parser.add_argument('id_vector', type=str, help='پالتی برای حذف انتخاب نشده',required=True)

class vector_resource(Resource):
    def post(self):
        idd = request.form['id']
        admin_validator(id=idd).admin_id_exists()
        keywords = request.form['keywords'].split('-')
        if len(keywords) == 0:
            return {'message':'کلمات کلیدی خالی است'},403
        jobs = request.form['jobs'].split(',')
        if len(jobs) == 0:
            return {'message':'دستبندی شغلی خالی است'},403
        logo_class = request.form['logo_class'].split(',')
        logo_class = [fact_class.find_by_name(x) for x in logo_class]
        if len(logo_class) == 0:
            return {'message':'نوع لوگو خالی است'},403
        file = request.files['file']
        file_type =  file.content_type
        file_name = file.filename
        temp_svg_patch = file_service.save_uploaded_file(request.files['file'])

        str_svg = vector_service.svg_file_to_string(temp_svg_patch)
        binary_svg = vector_service.svg_file_to_binary(temp_svg_patch)

        aspect_ratio_file = vector_service.aspect_ratio_file(temp_svg_patch)
        width_file = int(aspect_ratio_file['width'][:-2])
        height_file = int(aspect_ratio_file['height'][:-2])
        aspect_ratio_file = width_file / height_file
        
        aspect_ratio_content = vector_service.aspect_rate_content(temp_svg_patch)
        width_content = aspect_ratio_content['width']
        height_content = aspect_ratio_content['height']
        aspect_ratio_content = float(width_content) / float(height_content)
        existing_vector = vector.existing_file(file=file)
        if existing_vector:
            return {'message': 'فایل تکراری است'}, 409
        object_sent_vector = sent_vector()
        keywords = [object_sent_vector.normalize_word(x) for x in keywords]
        keywords_vector = [object_sent_vector.word_normaloize_and_vector_list(x) for x in keywords]
        jobs = [fact_jobs.find_by_name(x) for x in jobs]
        new_vector = vector(
            file = binary_svg,
            file_str = str_svg,
            file_name = file_name,
            file_type = file_type,
            jobs = [x['name'] for x in jobs],
            jobs_name = [x['title'] for x in jobs],
            jobs_name_vector = [x['vector'] for x in jobs],
            logo_class = [x['name'] for x in logo_class],
            logo_class_name = [x['title'] for x in logo_class],
            logo_class_name_vector = [x['vector'] for x in logo_class],
            keywords = keywords,
            keywords_vector = keywords_vector,
            creator = idd,
            aspect_ratio_file = aspect_ratio_file,
            width_file = width_file,
            height_file = height_file,
            aspect_ratio_content = aspect_ratio_content ,
            height_content = height_content,
            width_content = width_content,
        )
        new_vector.save()
        return True, 200
    def delete(self):
        args = del_vector_parser.parse_args()
        admin_validator(id=args['id']).admin_id_exists()
        result = vector.delete_vector(args['id_vector'])
        if result:
            return True, 200
        else:
            return {'message':'مورد یافت نشد برای حذف'},403

class vector_tank_resource(Resource):
    def post(self):
        args= vector_tank_parser.parse_args()
        admin_validator(id=args['id']).admin_id_exists()
        tank = vector.tank()
        return tank , 200