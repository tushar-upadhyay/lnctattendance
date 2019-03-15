import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

def main(username,password):
    s = requests.Session()
    url = "http://115.254.62.23/Accsoft2/Login.aspx?ctl00%24ScriptManager1=ctl00%24cph1%24UpdatePanel5%7Cctl00%24cph1%24btnStuLogin&ctl00%24cph1%24rdbtnlType=2&ctl00%24cph1%24txtStuUser=" + str(username) + "&ctl00%24cph1%24txtStuPsw=" + str(password) + "&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUJNzA0MDQwNTMxD2QWAmYPZBYCAgMPZBYEAgcPZBYGAgMPZBYCZg9kFgICAQ8QZGQWAQIBZAIFD2QWAmYPZBYCAgEPFgIeB1Zpc2libGVnZAIHD2QWAmYPZBYCAgEPFgIfAGgWBGYPZBYCZg9kFgICAQ9kFgJmD2QWAgIBDw8WAh4EVGV4dAULMTExNTY4MjM5NjhkZAIED2QWAmYPZBYCAgEPZBYCZg9kFgICAQ9kFgRmD2QWAmYPZBYCAgEPZBYCZg9kFgICAQ8QDxYGHg1EYXRhVGV4dEZpZWxkBQdGaW5ZZWFyHg5EYXRhVmFsdWVGaWVsZAUJRmluWWVhcklEHgtfIURhdGFCb3VuZGdkEBUPCi0tU2VsZWN0LS0KMjAxOS0yMDIwIAoyMDE4LTIwMTkgCjIwMTctMjAxOCAKMjAxNi0yMDE3IAoyMDE1LTIwMTYgCjIwMTQtMjAxNSAKMjAxMy0yMDE0IAoyMDEyLTIwMTMgCjIwMTEtMjAxMiAKMjAxMC0yMDExIAoyMDA5LTIwMTAgCjIwMDgtMjAwOSAKMjAwNy0yMDA4IAoyMDA2LTIwMDcgFQ8BMAIxNAIxMwIxMgIxMQIxMAE5ATgBNwE2ATUBNAEzATIBMRQrAw9nZ2dnZ2dnZ2dnZ2dnZ2cWAQICZAIBD2QWAmYPZBYCAgEPZBYCZg9kFgICAQ8QZGQWAGQCCQ8PFgIfAQULMjYtRmViLTIwMTlkZGSvCCL1v4Cju7Tiq%2FOFOQncQnRbljqL90N7tvNT6r1hiQ%3D%3D&__EVENTVALIDATION=%2FwEdAAfH7VlBBrgGcZPrivs60SbRM53Y8ZOLfkHDcm83dIGbmLHg4zuDo887rMmdulsCaAPs0I8Mn%2BYPuHswTYNssJXEVkWObqnKYQNrJjyTxcyx5%2FpqPUldr%2F0h7YqHATFqu3Du6Lub2srira%2Bf5x0vKRpFxAbaRNF9m3WP%2BO%2Bk9hHktcOShY04UlVWy%2FaL%2FBwQNLw%3D&__ASYNCPOST=true&ctl00%24cph1%24btnStuLogin=Login%20%3E%3E"
    mhtml = s.get(url).text
    soupm = BeautifulSoup(mhtml, 'html.parser')
    title = str(soupm.title.text)
    title = title.split()
    title.reverse()
    print(title[0])
    if title[0]=="DashBoard":
        name = soupm.findAll("td", {'class': "TopMenuTD_2"})[2].text.strip()
        fimgid = str(soupm.findAll("img")[3]['src'])
        da = fimgid.split(".")
        final = []
        for x in range(2, len(da)):
            final.append(da[x])
        finalurl = final[0] + "." + final[1]
        imageurl = "http://" + quote(("115.254.62.23/Accsoft2" + finalurl))
        attendenceurl = "http://115.254.62.23/Accsoft2/Parents/StuAttendanceStatus.aspx"
        ahtml = s.get(attendenceurl).text
        soupa = BeautifulSoup(ahtml, 'html.parser')
        total = soupa.find(id="ctl00_ContentPlaceHolder1_lbltotperiod").text
        attendence = soupa.find(id="ctl00_ContentPlaceHolder1_lbltotalp").text
        return [imageurl, name, total, attendence]
    else:
        return "error"


