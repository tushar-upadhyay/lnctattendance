import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
def subjectWise(username,password,lnctu=False):

    s = requests.Session()
    url = "http://portal.lnct.ac.in/Accsoft2/StudentLogin.aspx?ctl00%24ScriptManager1=ctl00%24cph1%24UpdatePanel5%7Cctl00%24cph1%24btnStuLogin&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUJLTk3NzUxOTMxD2QWAmYPZBYCAgMPZBYEAgcPZBYGAgcPZBYCZg9kFgICAQ8QZGQWAWZkAgkPZBYCZg9kFgICAQ8WAh4HVmlzaWJsZWcWAgIED2QWAmYPZBYCAgEPZBYCZg9kFgICAQ9kFgRmD2QWAmYPZBYCAgEPZBYCZg9kFgICAQ8QZGQWAGQCAQ9kFgJmD2QWAgIDDxYCHgVWYWx1ZQUCNTFkAgsPZBYCZg9kFgICAQ8WAh8AaBYCAgQPZBYCZg9kFgICAQ9kFgJmD2QWAgIBD2QWBGYPZBYCZg9kFgICAQ9kFgJmD2QWAgIBDxAPFgYeDURhdGFUZXh0RmllbGQFB0ZpblllYXIeDkRhdGFWYWx1ZUZpZWxkBQlGaW5ZZWFySUQeC18hRGF0YUJvdW5kZ2QQFQ8KLS1TZWxlY3QtLQoyMDE5LTIwMjAgCjIwMTgtMjAxOSAKMjAxNy0yMDE4IAoyMDE2LTIwMTcgCjIwMTUtMjAxNiAKMjAxNC0yMDE1IAoyMDEzLTIwMTQgCjIwMTItMjAxMyAKMjAxMS0yMDEyIAoyMDEwLTIwMTEgCjIwMDktMjAxMCAKMjAwOC0yMDA5IAoyMDA3LTIwMDggCjIwMDYtMjAwNyAVDwEwAjE0AjEzAjEyAjExAjEwATkBOAE3ATYBNQE0ATMBMgExFCsDD2dnZ2dnZ2dnZ2dnZ2dnZxYBAgFkAgEPZBYCZg9kFgICAQ9kFgJmD2QWAgIBDxBkZBYAZAIJDw8WAh4EVGV4dAULMjMtSmFuLTIwMjBkZGQjNMuk5EJq5qSPZq4EJBD6tB0pUuNkWeHCb1PHtBhULw%3D%3D&__EVENTVALIDATION=%2FwEdAAbizBDBTGYL1tI3qzYeuPAJseDjO4OjzzusyZ26WwJoA%2BzQjwyf5g%2B4ezBNg2ywlcRWRY5uqcphA2smPJPFzLHn%2Bmo9SV2v%2FSHtiocBMWq7cO7ou5vayuKtr5%2FnHS8pGkVcIkhB%2BazkX5InlwRHe1E7CMFQAS9GRJ3Y3jJTO15Clg%3D%3D&ctl00%24cph1%24rdbtnlType=2&ctl00%24cph1%24txtStuUser="+str(username) + "&ctl00%24cph1%24txtStuPsw=" + quote(str(password)) + "&__ASYNCPOST=true&ctl00%24cph1%24btnStuLogin=Login%20%3E%3E"
    if (lnctu == True):
        url = "http://accsoft.lnctu.ac.in/Accsoft2/Login.aspx?ctl00%24ScriptManager1=ctl00%24cph1%24UpdatePanel5%7Cctl00%24cph1%24btnStuLogin&ctl00%24cph1%24rdb=rdp&ctl00%24cph1%24txtStuUser=" +str(username) +"&ctl00%24cph1%24txtStuPsw=" + quote(password) + "&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwULLTEwNDk1ODMyMTYPZBYCZg9kFgICAw9kFgQCBw9kFgYCBw9kFgJmD2QWBAIBDxAPFgIeB0NoZWNrZWRoZGRkZAIDDxAPFgIfAGdkZGRkAgkPZBYCZg9kFgICAQ8WAh4HVmlzaWJsZWdkAgsPZBYCZg9kFgICAQ8WAh8BaBYGAgEPZBYCZg9kFgQCAQ8WAh4FVmFsdWUF6QF7CiAgImlwIjogIjI3LjYyLjE1MC4xNzQiLAogICJjaXR5IjogIlJhaXB1ciIsCiAgInJlZ2lvbiI6ICJDaGhhdHRpc2dhcmgiLAogICJjb3VudHJ5IjogIklOIiwKICAibG9jIjogIjIxLjIzMzMsODEuNjMzMyIsCiAgIm9yZyI6ICJBUzQ1NjA5IEJoYXJ0aSBBaXJ0ZWwgTHRkLiBBUyBmb3IgR1BSUyBTZXJ2aWNlIiwKICAicG9zdGFsIjogIjQ5MjAxMyIsCiAgInRpbWV6b25lIjogIkFzaWEvS29sa2F0YSIKfWQCAw8WAh8CBQ43MTEzZTU5OGZmNmU1OWQCAw9kFgJmD2QWAgIDDw8WAh8BaGRkAgQPZBYCZg9kFgICAQ9kFgJmD2QWAgIBD2QWBGYPZBYCZg9kFgICAQ9kFgJmD2QWAgIBDxAPFgYeDURhdGFUZXh0RmllbGQFB0ZpblllYXIeDkRhdGFWYWx1ZUZpZWxkBQlGaW5ZZWFySUQeC18hRGF0YUJvdW5kZ2QQFQwKLS1TZWxlY3QtLQoyMDE5LTIwMjAgCjIwMTgtMjAxOSAKMjAxNy0yMDE4IAoyMDE2LTIwMTcgCjIwMTUtMjAxNiAKMjAxNC0yMDE1IAoyMDEzLTIwMTQgCjIwMTItMjAxMyAKMjAxMS0yMDEyIAoyMDEwLTIwMTEgCjIwMDktMjAxMCAVDAEwAjExAjEwATkBOAE3ATYBNQE0ATMBMgExFCsDDGdnZ2dnZ2dnZ2dnZxYBAgFkAgEPZBYCZg9kFgICAQ9kFgJmD2QWAgIBDxBkZBYAZAIJDw8WAh4EVGV4dAULMDEtTWFyLTIwMjBkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAwUOY3RsMDAkY3BoMSRyZGYFDmN0bDAwJGNwaDEkcmRmBQ5jdGwwMCRjcGgxJHJkcBWJcaamtDeCXfaIrWtUKXuRZHXCCO1zJCcfy3F%2FmXNE&__EVENTVALIDATION=%2FwEWBgLby5ChAgKo4vbNDAL66OaeDALF29%2B1DQLwxNyhCALInIuCCA0XJI9riPA6nYs7KduveWs%2Fluwarj3KoEtaglr%2ByyII&__ASYNCPOST=true&ctl00%24cph1%24btnStuLogin=Login%20%3E%3E"
    mhtml = s.get(url).text
    soupm = BeautifulSoup(mhtml, 'html.parser')
    login = False
    try:
        title = str(soupm.title.text)
        title = title.split()
        title.reverse()
        print(title)
        if (len(title) > 0):
            if (title[0] == "DashBoard"):
                login = True
        else:
            login = True
    except:
        print('error')
    if login==True:
        attendenceurl = "http://portal.lnct.ac.in/Accsoft2/parents/subwiseattn.aspx"
        if(lnctu==True):
            attendenceurl = "http://accsoft.lnctu.ac.in/AccSoft2/parents/subwiseattn.aspx"
        ahtml = s.get(attendenceurl).text
        soupa = BeautifulSoup(ahtml, 'html.parser')
        htmlCollection = soupa.find_all('tr')
        result = []
        for x in range(18,len(htmlCollection)):
            data = htmlCollection[x].findChildren("td")
            result.append({
                'Subject':data[0].text,
                'TotalLectures':data[2].text,
                'Present':data[3].text,
                'Percentage':round(float(data[3].text)/float(data[2].text)*100,2)
            })
        return result
    else:
        return "error"

