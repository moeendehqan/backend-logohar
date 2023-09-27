import cv2
import string
import numpy as np
import random
import base64
import json
from cryptography.fernet import Fernet
import config
import datetime
from bson import ObjectId



key = b'MYZ2MqLhKxYhjPnwYlUBHqJUcVn5OHGXPHjjtG41Pco='
cipher_suite = Fernet(key)

def encrypt(message):
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message.decode()


def decrypt(encrypted_message):
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    return decrypted_message.decode()



def captchaGenerate():
    font = cv2.FONT_HERSHEY_COMPLEX
    captcha = np.zeros((40,140,3), np.uint8)
    captcha[:] = (255, 255, 255)#(random.randint(235,255),random.randint(245,255),random.randint(245,255))
    font= cv2.FONT_HERSHEY_SIMPLEX
    texcode = ''
    listCharector =  string.digits
    for i in range(1,5):
        bottomLeftCornerOfText = (random.randint(20,30)*i,35+(random.randint(-5,5)))
        fontScale= random.randint(5,12)/10
        fontColor= (random.randint(0,180),random.randint(50,180),random.randint(70,180))
        thickness= random.randint(1,2)
        lineType= random.randint(1,10)
        text = str(listCharector[random.randint(0,len(listCharector)-1)])
        texcode = texcode+(text)
        cv2.putText(captcha,text,bottomLeftCornerOfText,font,fontScale,fontColor,thickness,lineType)
        if random.randint(0,2)>0:
            pt1 = (random.randint(0,140),random.randint(0,40))
            pt2 = (random.randint(0,140),random.randint(0,40))
            lineColor = (random.randint(20,150),random.randint(40,150),random.randint(80,150))
            cv2.line(captcha,pt1,pt2,lineColor,1)
    stringImg = base64.b64encode(cv2.imencode('.jpg', captcha)[1]).decode()
    return [texcode,stringImg]



def captcha():
    cg = captchaGenerate()
    return json.dumps({'captcha':str(encrypt(cg[0])),'img':cg[1]})


def admin_login(request):
    data = request.get_json()

    data['captchaCode'] = decrypt(data['captchaCode'])
    if data['captchaCode'] != data['captchaInp']:
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
