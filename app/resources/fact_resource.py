from flask_restful import Resource, reqparse
from app.models.fact_color_type_models import fact_color_type
from app.models.fact_jobs_models import fact_jobs
from app.models.admin_user_models import admin_user
from app.models.fact_class_models import fact_class


class admin_color_type(Resource):
    def get(self):
        all_color_type = fact_color_type.get_all_color_type()
        for item in all_color_type:
            del item['vector']
        return all_color_type, 200





class admin_jobs(Resource):
    def get(self):
        all_jobs = fact_jobs.get_all()
        for item in all_jobs:
            del item['vector']
        return all_jobs, 200

class admin_class(Resource):
    def get(self):
        all_class = fact_class.get_all_class()
        for item in all_class:
            del item['vector']
        return all_class, 200
    


