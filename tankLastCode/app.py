import json
from flask import Flask, request
from flask_cors import CORS
import Authentication
import config
import basic
app = Flask(__name__)
CORS(app)


@app.route('/getcaptcha',methods = ['POST'])
def captcha():
    return Authentication.captcha()

@app.route('/admin/login',methods = ['POST'])
def admin_login():
    return Authentication.admin_login(request)

@app.route('/admin/checkid',methods = ['POST'])
def admin_checkid():
    return Authentication.admin_checkid(request)

@app.route('/admin/getinfouser',methods = ['POST'])
def admin_getinfouser():
    return Authentication.admin_getinfouser(request.get_json())

@app.route('/admin/setpallet',methods = ['POST'])
def admin_setpallet():
    return basic.admin_setpallet(request.get_json())

@app.route('/admin/getstaticspallet',methods = ['POST'])
def admin_getstaticspallet():
    return basic.admin_getstaticspallet(request.get_json())

@app.route('/admin/getbankpallet',methods = ['POST'])
def admin_getbankpallet():
    return basic.admin_getbankpallet(request.get_json())

@app.route('/public/getallcategory',methods = ['get'])
def public_getallcategory():
    return json.dumps({'colorType':config.categoryColor,'jobType':config.categoryJob})


@app.route('/admin/setvector',methods = ['POST'])
def admin_setvector():
    id = request.form.get('id')
    id_vector = request.form.get('idVector')
    file_vector = request.files['fileVector']  # یک فایل
    type_job_vector = request.form.get('typeJobVector')
    keywords = request.form.get('keywords')
    return basic.admin_setvector(id, id_vector, file_vector, type_job_vector, keywords)


@app.route('/admin/getvectorbank',methods = ['POST'])
def admin_getvectorbank():
    return basic.admin_getvectorbank(request.get_json())

@app.route('/admin/setfont',methods = ['POST'])
def admin_setfont():
    id = request.form.get('id')
    font_id = request.form.get('font_id')
    file = request.files['file']  # یک فایل
    typeJob = request.form.get('typeJob')
    weight = request.form.get('weight')
    name = request.form.get('name')
    return basic.admin_setfont(id, font_id, file, typeJob, weight, name)

@app.route('/admin/getfontsname',methods = ['POST'])
def admin_getfontsname():
    return basic.admin_getfontsname(request.get_json())

@app.route('/admin/getfontsbank',methods = ['POST'])
def admin_getfontsbank():
    return basic.admin_getfontsbank(request.get_json())

if __name__ == '__main__':
    #serve(app, host="0.0.0.0", port=2100,threads= 8)
    app.run(host='0.0.0.0', debug=True)