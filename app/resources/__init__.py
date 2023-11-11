from flask_restful import Api
from .captcha_resource import captcha_Resource
from .login_resource import admin_cookie_check_resource, admin_login_resource
from .fact_resource import admin_color_type, admin_jobs, admin_class
from .pallet_resource import pallet_tank_resource, pallet_resource
from .vector_resource import vector_resource,vector_tank_resource
from .font_resource import font_resource , font_tank_resource
from .validation_resource import BusinessName_resource, Keywords_resource

api = Api()
api.add_resource(captcha_Resource, '/captcha')
api.add_resource(admin_cookie_check_resource, '/admin/cookie_check')
api.add_resource(admin_login_resource, '/admin/login')
api.add_resource(admin_color_type, '/admin/colortypes')
api.add_resource(admin_jobs, '/admin/jobs')
api.add_resource(pallet_tank_resource, '/admin/pallettank')
api.add_resource(pallet_resource, '/admin/pallet')
api.add_resource(vector_resource, '/admin/vector')
api.add_resource(vector_tank_resource, '/admin/vectortank')
api.add_resource(font_resource, '/admin/font')
api.add_resource(font_tank_resource, '/admin/fonttank')
api.add_resource(admin_class, '/admin/class')

api.add_resource(BusinessName_resource, '/validtion/name')
api.add_resource(Keywords_resource, '/validtion/keywords')

