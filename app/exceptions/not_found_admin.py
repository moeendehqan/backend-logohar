from flask_restful import abort
from app.models.admin_user_models import admin_user



class admin_validator:
    def __init__(self,id):
        self.id = id

    def admin_id_exists(self):
        result = admin_user.find_by_id_string(self.id)
        
        if result is None:
            abort(403,message='ادمین یافت نشد، لطفا مجددا وارد شود')


