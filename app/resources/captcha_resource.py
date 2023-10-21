from flask_restful import Resource, reqparse
from GuardPyCaptcha.Captch import GuardPyCaptcha

class captcha_Resource(Resource):
    def get(self):
        Captcha = GuardPyCaptcha()
        Captcha = Captcha.Captcha_generation(num_char=4,only_num=True)
        return Captcha,200