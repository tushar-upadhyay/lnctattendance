from firebase import Firebase
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import quote,unquote
from cryptography.fernet import  Fernet
import os
f = Fernet(bytes(str(os.getenv('fernet_key')).encode()))
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
def getName(username,password,token=None,lnctu=False):
    s = requests.Session()
    url = "http://portal.lnct.ac.in/Accsoft2/StudentLogin.aspx?ctl00%24ScriptManager1=ctl00%24cph1%24UpdatePanel5%7Cctl00%24cph1%24btnStuLogin&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUJLTk3NzUxOTMxD2QWAmYPZBYCAgMPZBYEAgcPZBYGAgcPZBYCZg9kFgICAQ8QZGQWAWZkAgkPZBYCZg9kFgICAQ8WAh4HVmlzaWJsZWcWAgIED2QWAmYPZBYCAgEPZBYCZg9kFgICAQ9kFgRmD2QWAmYPZBYCAgEPZBYCZg9kFgICAQ8QZGQWAGQCAQ9kFgJmD2QWAgIDDxYCHgVWYWx1ZQUCNTFkAgsPZBYCZg9kFgICAQ8WAh8AaBYCAgQPZBYCZg9kFgICAQ9kFgJmD2QWAgIBD2QWBGYPZBYCZg9kFgICAQ9kFgJmD2QWAgIBDxAPFgYeDURhdGFUZXh0RmllbGQFB0ZpblllYXIeDkRhdGFWYWx1ZUZpZWxkBQlGaW5ZZWFySUQeC18hRGF0YUJvdW5kZ2QQFQ8KLS1TZWxlY3QtLQoyMDE5LTIwMjAgCjIwMTgtMjAxOSAKMjAxNy0yMDE4IAoyMDE2LTIwMTcgCjIwMTUtMjAxNiAKMjAxNC0yMDE1IAoyMDEzLTIwMTQgCjIwMTItMjAxMyAKMjAxMS0yMDEyIAoyMDEwLTIwMTEgCjIwMDktMjAxMCAKMjAwOC0yMDA5IAoyMDA3LTIwMDggCjIwMDYtMjAwNyAVDwEwAjE0AjEzAjEyAjExAjEwATkBOAE3ATYBNQE0ATMBMgExFCsDD2dnZ2dnZ2dnZ2dnZ2dnZxYBAgFkAgEPZBYCZg9kFgICAQ9kFgJmD2QWAgIBDxBkZBYAZAIJDw8WAh4EVGV4dAULMjMtSmFuLTIwMjBkZGQjNMuk5EJq5qSPZq4EJBD6tB0pUuNkWeHCb1PHtBhULw%3D%3D&__EVENTVALIDATION=%2FwEdAAbizBDBTGYL1tI3qzYeuPAJseDjO4OjzzusyZ26WwJoA%2BzQjwyf5g%2B4ezBNg2ywlcRWRY5uqcphA2smPJPFzLHn%2Bmo9SV2v%2FSHtiocBMWq7cO7ou5vayuKtr5%2FnHS8pGkVcIkhB%2BazkX5InlwRHe1E7CMFQAS9GRJ3Y3jJTO15Clg%3D%3D&ctl00%24cph1%24rdbtnlType=2&ctl00%24cph1%24txtStuUser="+str(username) + "&ctl00%24cph1%24txtStuPsw=" + quote(str(password)) + "&__ASYNCPOST=true&ctl00%24cph1%24btnStuLogin=Login%20%3E%3E"
    if(lnctu==True):
        url = "http://accsoft.lnctu.ac.in/Accsoft2/Login.aspx?ctl00%24ScriptManager1=ctl00%24cph1%24UpdatePanel5%7Cctl00%24cph1%24btnStuLogin&ctl00%24cph1%24rdb=rdp&ctl00%24cph1%24txtStuUser=" +str(username) +"&ctl00%24cph1%24txtStuPsw=" + quote(password) + "&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwULLTEwNDk1ODMyMTYPZBYCZg9kFgICAw9kFgQCBw9kFgYCBw9kFgJmD2QWBAIBDxAPFgIeB0NoZWNrZWRoZGRkZAIDDxAPFgIfAGdkZGRkAgkPZBYCZg9kFgICAQ8WAh4HVmlzaWJsZWdkAgsPZBYCZg9kFgICAQ8WAh8BaBYGAgEPZBYCZg9kFgQCAQ8WAh4FVmFsdWUF6QF7CiAgImlwIjogIjI3LjYyLjE1MC4xNzQiLAogICJjaXR5IjogIlJhaXB1ciIsCiAgInJlZ2lvbiI6ICJDaGhhdHRpc2dhcmgiLAogICJjb3VudHJ5IjogIklOIiwKICAibG9jIjogIjIxLjIzMzMsODEuNjMzMyIsCiAgIm9yZyI6ICJBUzQ1NjA5IEJoYXJ0aSBBaXJ0ZWwgTHRkLiBBUyBmb3IgR1BSUyBTZXJ2aWNlIiwKICAicG9zdGFsIjogIjQ5MjAxMyIsCiAgInRpbWV6b25lIjogIkFzaWEvS29sa2F0YSIKfWQCAw8WAh8CBQ43MTEzZTU5OGZmNmU1OWQCAw9kFgJmD2QWAgIDDw8WAh8BaGRkAgQPZBYCZg9kFgICAQ9kFgJmD2QWAgIBD2QWBGYPZBYCZg9kFgICAQ9kFgJmD2QWAgIBDxAPFgYeDURhdGFUZXh0RmllbGQFB0ZpblllYXIeDkRhdGFWYWx1ZUZpZWxkBQlGaW5ZZWFySUQeC18hRGF0YUJvdW5kZ2QQFQwKLS1TZWxlY3QtLQoyMDE5LTIwMjAgCjIwMTgtMjAxOSAKMjAxNy0yMDE4IAoyMDE2LTIwMTcgCjIwMTUtMjAxNiAKMjAxNC0yMDE1IAoyMDEzLTIwMTQgCjIwMTItMjAxMyAKMjAxMS0yMDEyIAoyMDEwLTIwMTEgCjIwMDktMjAxMCAVDAEwAjExAjEwATkBOAE3ATYBNQE0ATMBMgExFCsDDGdnZ2dnZ2dnZ2dnZxYBAgFkAgEPZBYCZg9kFgICAQ9kFgJmD2QWAgIBDxBkZBYAZAIJDw8WAh4EVGV4dAULMDEtTWFyLTIwMjBkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAwUOY3RsMDAkY3BoMSRyZGYFDmN0bDAwJGNwaDEkcmRmBQ5jdGwwMCRjcGgxJHJkcBWJcaamtDeCXfaIrWtUKXuRZHXCCO1zJCcfy3F%2FmXNE&__EVENTVALIDATION=%2FwEWBgLby5ChAgKo4vbNDAL66OaeDALF29%2B1DQLwxNyhCALInIuCCA0XJI9riPA6nYs7KduveWs%2Fluwarj3KoEtaglr%2ByyII&__ASYNCPOST=true&ctl00%24cph1%24btnStuLogin=Login%20%3E%3E"
    mhtml = s.get(url).text
    soupm = BeautifulSoup(mhtml, 'html.parser')
    login = False
    try:
        title = str(soupm.title.text)
        title = title.split()
        title.reverse()
        print(title)
        if(len(title)>0):
            if(title[0]=="DashBoard"):
                login = True
        else:
            login=True
    except:
        print('error')
    # if login==True and lnctu==False:
    #     name = soupm.findAll("td", {'class': "TopMenuTD_2"})[2].text.strip()
    #     college = soupm.findAll("td", {'class': "LoginInfo"})[0].text.strip()
    #     section = soupm.findAll("td", {'class': "TopMenuTD_2"})[8].text.strip()
    #     rawData  = soupm.find_all("td",{'class':"TopMenuTD_2"})[6].text.strip()
    #     branch = re.sub('[^A-Za-z0 ]+', '', rawData).strip("BTech  Sem")
    #     Semester = re.sub('[^1-9]+', '', rawData)
    #     fimgid = str(soupm.findAll("img")[3]['src'])
    #     password = unquote(password)
    #     password = password.encode()
    #     passwordEncrypted = f.encrypt(password).decode()
    #     try:
    #         database.child(name).set({
    #             "username":username,
    #             "password":passwordEncrypted,
    #             "token":token
    #         })
    #     except:
    #         database.child('dottedNames/'+username).set({
    #             'name':name,
    #             'password':passwordEncrypted,
    #             'token':token
    #         })
    #     da = fimgid.split(".")
    #     final = []
    #     try:
    #         for x in range(2, len(da)):
    #             final.append(da[x])
    #         finalurl = final[0] + "." + final[1]
    #         imageurl = "http://" + quote(("portal.lnct.ac.in/Accsoft2" + finalurl))
    #         return [imageurl,name,college,Semester,branch,section]
    #     except:
    #         imageurl = "https://banner2.kisspng.com/20180920/efk/kisspng-user-logo-information-service-design-5ba34f88a0c3a6.5907352915374293846585.jpg"
    #         return [imageurl,name,college,Semester,branch,section]
    if(login==True):
        name = soupm.findAll("span", {'class': "mr-2 d-none d-lg-inline text-gray-600 small"})[0].text.strip()
        college = "LNCT"
        if(lnctu):
            college='LNCTU'
        data = soupm.findAll("a", {'class': "nav-link dropdown-toggle"})[2].text.strip()
        semester = None
        fimgid = soupm.findAll('img',{'class':'img-profile rounded-circle'})[0]['src']
        password = unquote(password)
        password = password.encode()
        passwordEncrypted = f.encrypt(password).decode()
        try:
            database.child(name).set({
                "username":username,
                "college":college,
                "token":token,
                "password":passwordEncrypted
            })
        except:
            try:
                database.child('dottedNames/' + username).set({
                                'name':name,
                                'password':passwordEncrypted,
                                'token':token
                                })
            except:
                print('db error')
        for x in data:
            if(x.isdigit()):
                semester=x
        da = fimgid.split(".")
        final = []
        try:
            for x in range(2, len(da)):
                final.append(da[x])
            finalurl = final[0] + "." + final[1]
            imageurl = "http://" + quote(("portal.lnct.ac.in/Accsoft2" + finalurl))
            if (lnctu == True):
                imageurl = "http://" + quote(("accsoft.lnctu.ac.in/Accsoft2" + finalurl))
            return [imageurl, name, college, semester, '', '']
        except:
            imageurl = "https://banner2.kisspng.com/20180920/efk/kisspng-user-logo-information-service-design-5ba34f88a0c3a6.5907352915374293846585.jpg"
            return [imageurl, name, college, semester, '', '']
    else:
        database.child("failedAttempts/"+username).set({
            'triedPassword':password
        })
        return "error"
