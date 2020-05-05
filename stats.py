import os
from firebase import Firebase
config = {
    'apiKey': str(os.getenv('apiKey2')),
    'authDomain': "app-token.firebaseapp.com",
    'databaseURL': "https://app-token.firebaseio.com",
    'projectId': "app-token",
    'storageBucket': "app-token.appspot.com",
    'messagingSenderId': str(os.getenv('messageid2')),
    'appId': str(os.getenv('appid2'))
}
firebase = Firebase(config)
database = firebase.database()
def getUsers():
    count = 0
    users =database.child().get().val()
    for x in users:
        data = dict(users[x])
        username = data.get("username")
        if(username):
            count = count+1
    return count
def getLogouts():
    return dict(database.child("Logouts").get().val()).__len__()
def getTotalRequests():
    return database.child("stats/totalRequests").get().val()
def getFailedAttempts():
    try:
        return dict(database.child("failedAttempts").get().val()).__len__()
    except:
        return 0
