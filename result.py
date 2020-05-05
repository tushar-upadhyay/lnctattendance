import requests
from bs4 import BeautifulSoup
from getCaptcha import getCaptcha
from getHeaders import getHeaders
import time
from ocr import detect_text_uri
session  = requests.Session()
def getResult(rollNo,semester,results,errors):
    html =session.post("http://result.rgpv.ac.in/Result/ProgramSelect.aspx",data={
    '__EVENTTARGET': 'radlstProgram$1',
    '__EVENTARGUMENT':'',
    '__LASTFOCUS':'',
    '__VIEWSTATE':getHeaders()[0],
    '__VIEWSTATEGENERATOR': 'F697B5F5',
    '__EVENTVALIDATION':getHeaders()[1],
    'radlstProgram': '24'
    })
    html = html.text
    soup  =  BeautifulSoup(html, 'html.parser')
    imageUrl = "http://result.rgpv.ac.in/Result/"
    imageUrl = imageUrl + soup.findAll("img")[1]['src']
    captcha = detect_text_uri(imageUrl)
    import random
    time.sleep(random.random()+5)
    if(captcha=="Error"):
        errors.append({'title':rollNo})
    else:
        image = captcha.rstrip()
        data = {
        '__VIEWSTATE':soup.find(id ="__VIEWSTATE").get('value'),
        '__EVENTVALIDATION':soup.find(id ="__EVENTVALIDATION").get('value'),
        '__VIEWSTATEGENERATOR':soup.find(id ="__VIEWSTATEGENERATOR").get('value'),
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        'ctl00$ContentPlaceHolder1$txtrollno': str(rollNo),
        'ctl00$ContentPlaceHolder1$drpSemester': str(semester),
        'ctl00$ContentPlaceHolder1$rbtnlstSType': 'G',
        'ctl00$ContentPlaceHolder1$TextBox1': str(image),
        'ctl00$ContentPlaceHolder1$btnviewresult': 'View+Result'
        }
        finalhtml = session.post("http://result.rgpv.ac.in/Result/BErslt.aspx",data=data).text
        result = BeautifulSoup(finalhtml,'html.parser')
        try:
            name  = result.find(id="ctl00_ContentPlaceHolder1_lblNameGrading").text.strip()
            SGPA = result.find(id="ctl00_ContentPlaceHolder1_lblSGPA").text
            CGPA  = result.find(id="ctl00_ContentPlaceHolder1_lblcgpa").text

            results.append({'title':rollNo,'data':[{'Name':name},{'SGPA':SGPA},{'CGPA':CGPA}]})
        except:
            errors.append({'title':rollNo})
