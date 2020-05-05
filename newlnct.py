import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
from firebase import Firebase
import datetime
from urllib.parse import quote,unquote
from cryptography.fernet import  Fernet
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
db = firebase.database()
def newlnct(username, password):
    s = requests.Session()
    url = "http://portal.lnct.ac.in/Accsoft2/StudentLogin.aspx?ctl00%24ScriptManager1=ctl00%24cph1%24UpdatePanel5%7Cctl00%24cph1%24btnStuLogin&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUJLTk3NzUxOTMxD2QWAmYPZBYCAgMPZBYEAgcPZBYGAgcPZBYCZg9kFgICAQ8QZGQWAWZkAgkPZBYCZg9kFgICAQ8WAh4HVmlzaWJsZWcWAgIED2QWAmYPZBYCAgEPZBYCZg9kFgICAQ9kFgRmD2QWAmYPZBYCAgEPZBYCZg9kFgICAQ8QZGQWAGQCAQ9kFgJmD2QWAgIDDxYCHgVWYWx1ZQUCNTFkAgsPZBYCZg9kFgICAQ8WAh8AaBYCAgQPZBYCZg9kFgICAQ9kFgJmD2QWAgIBD2QWBGYPZBYCZg9kFgICAQ9kFgJmD2QWAgIBDxAPFgYeDURhdGFUZXh0RmllbGQFB0ZpblllYXIeDkRhdGFWYWx1ZUZpZWxkBQlGaW5ZZWFySUQeC18hRGF0YUJvdW5kZ2QQFQ8KLS1TZWxlY3QtLQoyMDE5LTIwMjAgCjIwMTgtMjAxOSAKMjAxNy0yMDE4IAoyMDE2LTIwMTcgCjIwMTUtMjAxNiAKMjAxNC0yMDE1IAoyMDEzLTIwMTQgCjIwMTItMjAxMyAKMjAxMS0yMDEyIAoyMDEwLTIwMTEgCjIwMDktMjAxMCAKMjAwOC0yMDA5IAoyMDA3LTIwMDggCjIwMDYtMjAwNyAVDwEwAjE0AjEzAjEyAjExAjEwATkBOAE3ATYBNQE0ATMBMgExFCsDD2dnZ2dnZ2dnZ2dnZ2dnZxYBAgFkAgEPZBYCZg9kFgICAQ9kFgJmD2QWAgIBDxBkZBYAZAIJDw8WAh4EVGV4dAULMjMtSmFuLTIwMjBkZGQjNMuk5EJq5qSPZq4EJBD6tB0pUuNkWeHCb1PHtBhULw%3D%3D&__EVENTVALIDATION=%2FwEdAAbizBDBTGYL1tI3qzYeuPAJseDjO4OjzzusyZ26WwJoA%2BzQjwyf5g%2B4ezBNg2ywlcRWRY5uqcphA2smPJPFzLHn%2Bmo9SV2v%2FSHtiocBMWq7cO7ou5vayuKtr5%2FnHS8pGkVcIkhB%2BazkX5InlwRHe1E7CMFQAS9GRJ3Y3jJTO15Clg%3D%3D&ctl00%24cph1%24rdbtnlType=2&ctl00%24cph1%24txtStuUser="+str(username) + "&ctl00%24cph1%24txtStuPsw=" + quote(str(password)) + "&__ASYNCPOST=true&ctl00%24cph1%24btnStuLogin=Login%20%3E%3E"
    mhtml = s.get(url).text
    soupm = BeautifulSoup(mhtml, 'html.parser')
    title = str(soupm.title.text)
    title = title.split()
    title.reverse()
    print(title)
    if title==[]:
        name = soupm.findAll("span", {'class': "mr-2 d-none d-lg-inline text-gray-600 small"})[0].text.strip()
        data = soupm.findAll("a", {'class': "nav-link dropdown-toggle"})[2].text.strip()
        fimgid = soupm.findAll('img', {'class': 'img-profile rounded-circle'})[0]['src']
        da = fimgid.split(".")
        final = []
        try:
            for x in range(2, len(da)):
                final.append(da[x])
            finalurl = final[0] + "." + final[1]
            imageurl = "http://" + quote(("portal.lnct.ac.in/Accsoft2" + finalurl))
        except:
            imageurl = "https://banner2.kisspng.com/20180920/efk/kisspng-user-logo-information-service-design-5ba34f88a0c3a6.5907352915374293846585.jpg"
        password = unquote(password)
        password = password.encode()
        passwordEncrypted = f.encrypt(password).decode()
        db.child(username).update({
            "name": name,
            "password": passwordEncrypted,
            'loggedout':'False'
        })
        attendenceurl = "http://portal.lnct.ac.in/Accsoft2/Parents/StuAttendanceStatus.aspx"
        ahtml = s.get(attendenceurl).text
        soupa = BeautifulSoup(ahtml, 'html.parser')
        total = soupa.find(id="ctl00_ContentPlaceHolder1_lbltotperiod").text
        attendence = soupa.find(id="ctl00_ContentPlaceHolder1_lbltotalp").text
        import re
        attendence = int(re.findall(r'\d+', attendence)[0])
        total = int(re.findall(r'\d+', total)[0])
        return [imageurl, name, total, attendence]
    else:
        return "error"

