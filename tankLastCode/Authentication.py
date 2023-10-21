import cv2
import string
import numpy as np
import random
import keyring

import json
from cryptography.fernet import Fernet
import config
import datetime
from bson import ObjectId
from GuardPyCaptcha.Captch import GuardPyCaptcha




        
        
key = b'MYZ2MqLhKxYhjPnwYlUBHqJUcVn5OHGXPHjjtG41Pco='
cipher_suite = Fernet(key)

def encrypt(message):
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message.decode()

def decrypt(encrypted_message):
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    return decrypted_message.decode()


def captcha():
    cp = GuardPyCaptcha()
    cp = cp.Captcha_generation(num_char=4,only_num=True)
    return json.dumps({'captcha':cp['encrypted_response'],'img':cp['image']})


def admin_login(request):
    data = request.get_json()
    cp = GuardPyCaptcha()
    if not cp.check_response(data['captchaCode'],data['captchaInp']):
        config.db['logAdminLogin'].insert_one({'username':data['username'],'password':data['password'],'date':datetime.datetime.now(),'result':False,'ip':request.remote_addr,'User-Agent':request.headers.get('User-Agent'),'msg':'کد کپچا اشتباه است'})
        return json.dumps({'reply':False,'msg':'کد کپچا اشتباه است'})
    del data['captchaCode']
    del data['captchaInp']
    adminDict = config.db['adminUser'].find_one({'username':data['username'],'password':data['password']})
    if adminDict == None:
        config.db['logAdminLogin'].insert_one({'username':data['username'],'password':data['password'],'date':datetime.datetime.now(),'result':False,'ip':request.remote_addr,'User-Agent':request.headers.get('User-Agent'),'msg':'نام کاربری یا رمز عبور یافت نشد'})
        return json.dumps({'reply':False,'msg':'نام کاربری یا رمز عبور یافت نشد'})
    config.db['logAdminLogin'].insert_one({'username':data['username'],'password':data['password'],'date':datetime.datetime.now(),'result':True,'ip':request.remote_addr,'User-Agent':request.headers.get('User-Agent'),'msg':''})
    return json.dumps({'reply':True,'id':str(adminDict['_id'])})



def admin_checkid(request):
    try:
        data = request.get_json()
        _id = ObjectId(data['id'])
        adminDict = config.db['adminUser'].find_one({'_id':_id})
        if adminDict == None:
            return json.dumps({'reply':False})
        return json.dumps({'reply':True})
    except:
        return json.dumps({'reply':False})


def admin_getinfouser(data):
    try:
        _id = ObjectId(data['id'])
        adminDict = config.db['adminUser'].find_one({'_id':_id},{'_id':0,'name':1})
        if adminDict == None:
            return json.dumps({'reply':False,'msg':'کاربری یافت نشد'})
        return json.dumps({'reply':True,'infouser':adminDict})
    except:
        return json.dumps({'reply':False,'msg':'کاربری یافت نشد'})
