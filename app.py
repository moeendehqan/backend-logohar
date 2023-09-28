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


@app.route('/public/getallcategory',methods = ['POST'])
def public_getallcategory():
    return json.dumps({'colorType':config.categoryColor,'jobType':config.categoryJob})

if __name__ == '__main__':
    #serve(app, host="0.0.0.0", port=2100,threads= 8)
    app.run(host='0.0.0.0', debug=True)