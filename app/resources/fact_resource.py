from flask_restful import Resource, reqparse
from app.models.fact_color_type_models import fact_color_type
from app.models.fact_jobs_models import fact_jobs
from app.models.admin_user_models import admin_user


class admin_color_type(Resource):
    def get(self):
        all_color_type = fact_color_type.get_all_color_type()
        for item in all_color_type:
            del item['vector']
        return all_color_type, 200





class admin_jobs(Resource):
    def get(self):
        all_category = fact_jobs.get_all()
        for item in all_category:
            del item['vector']
        return all_category, 200


