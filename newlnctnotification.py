from pyfcm import FCMNotification
from firebase import Firebase
from cryptography.fernet import  Fernet
from attendance import main
import os
f = Fernet(bytes(str(os.getenv('fernet_key')).encode()))
config = {
    "apiKey": str(os.getenv('apiKey1')),
    "authDomain": "lnctdata.firebaseapp.com",
    "databaseURL": "https://lnctdata.firebaseio.com",
    "projectId": "lnctdata",
    "storageBucket": "lnctdata.appspot.com",
    "messagingSenderId": str(os.getenv('messageid1')),
    "databaseURL": "https://lnctdata.firebaseio.com"
}
firebase = Firebase(config)
database = firebase.database()
def getAttendance():
    users = database.child().get().val()
    for x in users:
        data = dict(users[x])
        token = data.get('token')
        loggedout = data.get('loggedout')
        if(token and loggedout=='False'):
            password = f.decrypt(data.get('password').encode())
            attendance = main(x, password.decode())
            send(token,data.get('name'),attendance)
push_service = FCMNotification(api_key=str(os.getenv('fcmkey')))
def send(registration_id,name,attendance):
    message_title = 'Hey '+ name + '!'
    message_body = "Your attendance is "+str(attendance) +'%'
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)