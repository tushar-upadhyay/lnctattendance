
from multiprocessing import Process,Manager
import requests
from urllib.parse import quote
from firebase import Firebase
from attendance import main
from cryptography.fernet import  Fernet
import os
f = Fernet(bytes(str(os.getenv('fernet_key')).encode()))
config = {
    'apiKey':str(os.getenv('apiKey2')),

    'authDomain': "app-token.firebaseapp.com",
    'databaseURL': "https://app-token.firebaseio.com",
    'projectId': "app-token",
    'storageBucket': "app-token.appspot.com",
    'messagingSenderId': str(os.getenv('messageid2')),
    'appId': str(os.getenv('appid2'))
}
firebase = Firebase(config)
database = firebase.database()
# Basic arguments. You should extend this function with the push features you
# want to use, or simply pass in a `PushMessage` object.
def send_push_message(token,title, message, extra=None):
    try:
        res = requests.post("https://exp.host/--/api/v2/push/send",json={
            "to":token,
            "title":"Hey " + title + "!",
            "body":"Your attendance is "+message + " %"
        })
        return (res.json())
    except:
        return ("error")
def finallySend(start,end):
    users = database.child().get().val()
    counter = 0
    for x in users:
        if(counter>=start and counter<=end):
            data = dict(users[x])
            token = data.get('token')
            username = data.get('username')
            if(username and token):
                try:
                    password = f.decrypt(data.get('password').encode())
                    # print(username)
                    attendance = main(username,password.decode())
                    res = send_push_message(str(token),str(x),str(attendance))
                    print(x, res['data']['status'])
                    # bar.next()
                except:
                        print("error: in "+username)
        counter = counter+1
def start(s):
    p1 = Process(target=finallySend,args=(s,s+10))
    p2 = Process(target=finallySend,args=(s+11,s+20))
    p3  =Process(target=finallySend,args=(s+21,s+30))
    p4 = Process(target=finallySend,args=(s+31,s+40))
    p5 = Process(target=finallySend,args=(s+41,s+50))
    p6 = Process(target=finallySend,args=(s+51,s+60))
    p7 = Process(target=finallySend,args=(s+61,s+70))
    p8 = Process(target=finallySend,args=(s+71,s+80))
    p9 = Process(target=finallySend,args=(s+81,s+90))
    p10 =Process(target=finallySend,args=(s+91,s+100))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()
def finallyStart():
    length = database.child().get().val().__len__()
    for x in range(0,length+1,101):
        start(x)
