import json
from flask import Flask, request
from flask_cors import CORS
import Authentication

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

if __name__ == '__main__':
    #serve(app, host="0.0.0.0", port=2100,threads= 8)
    app.run(host='0.0.0.0', debug=True)