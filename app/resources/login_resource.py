from flask_restful import Resource, reqparse
from GuardPyCaptcha.Captch import GuardPyCaptcha
from bson import ObjectId
from app.models.admin_user_models import admin_user
from app.exceptions.not_found_admin import admin_validator
admin_cookie_parser = reqparse.RequestParser()
admin_cookie_parser.add_argument('id', type=str, help='ای دی که در کوکی ذخیره شده است')

admin_login_parser = reqparse.RequestParser()
admin_login_parser.add_argument('username', type=str, help='نام کاربری')
admin_login_parser.add_argument('password', type=str, help='رمزعبور')
admin_login_parser.add_argument('captchaInp', type=str, help='پاسخ کاربر به کپچا')
admin_login_parser.add_argument('captchaCode', type=str, help='پاسخ رمز شده کپچا')


class admin_cookie_check_resource(Resource):
    def post(self):
        args = admin_cookie_parser.parse_args()
        found_user = admin_user.find_by_id_string(args['id'])
        if found_user:
            return found_user, 200
        else:
            return {'message':'کاربر یافت نشد'},403
    
class admin_login_resource(Resource):
    def post(self):
        args = admin_login_parser.parse_args()
        captcha = GuardPyCaptcha()
        if not captcha.check_response(args['captchaCode'],args['captchaInp']):
            return {'message':'کدکچپا صحیح نیست'},403
        else:
            found_user = admin_user.find_by_username_and_password(args['username'], args['password'])
            if found_user:
                return found_user, 200
            else:
                return {'message':'کاربر یافت نشد'}, 403




