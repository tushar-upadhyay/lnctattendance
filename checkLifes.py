from firebase import Firebase
from datetime import datetime
from pytz import timezone

import os
config = {
    'apiKey': str(os.getenv('apiKey3')),
    'authDomain': "testing-f442d.firebaseapp.com",
    'databaseURL': "https://testing-f442d.firebaseio.com",
    'projectId': "testing-f442d",
    'storageBucket': "testing-f442d.appspot.com",
}
firebase = Firebase(config)
database = firebase.database()

def getLife(id,check=False):
    india = timezone('Asia/Kolkata')
    raw_time = datetime.now(india)
    minute = int(raw_time.strftime('%M'))
    rem = minute%15
    q = int(minute/15)*15
    if rem>8:
        q=q+15
    hour = raw_time.strftime('%H')
    try:

        try:
            current_users = database.child('data').child(hour).child(q).get().val()['users']
            database.child('data').child(hour).child(q).update({'users':current_users+1})
        except:
            database.child('data').child(hour).child(q).set({'users': 1})
        life =  int(database.child(id).get().val()['lifes'])
        if(life>0 and check==False):
            database.child(id).update({'lifes':life-1})
        return life
    except:
        database.child(id).set({'lifes':5})
        return 5
