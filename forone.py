import requests
import time
from bs4 import BeautifulSoup
from getHeaders import getHeaders
from ocr import detect_text_uri
session  = requests.Session()
def forone(rollNo,semester):
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
    captcha = captcha.rstrip()
    if(captcha=="Error"):
        return "Error"
    else:
        image = captcha
        data = {
        '__VIEWSTATE':soup.find(id ="__VIEWSTATE").get('value'),
        '__EVENTVALIDATION':soup.find(id ="__EVENTVALIDATION").get('value'),
        '__VIEWSTATEGENERATOR':soup.find(id ="__VIEWSTATEGENERATOR").get('value'),
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        'ctl00$ContentPlaceHolder1$txtrollno': str(rollNo),
        'ctl00$ContentPlaceHolder1$drpSemester': str(semester),
        'ctl00$ContentPlaceHolder1$rbtnlstSType': 'G',
        'ctl00$ContentPlaceHolder1$TextBox1': image,
        'ctl00$ContentPlaceHolder1$btnviewresult': 'View+Result'
        }
        time.sleep(4)
        finalhtml = session.post("http://result.rgpv.ac.in/Result/BErslt.aspx",data=data).text
        result = BeautifulSoup(finalhtml,'html.parser')
        try:
            _data = result.find_all("tr")[15]
            _finaldata = _data.find_all('tr')
            _final_result = []
            name  = result.find(id="ctl00_ContentPlaceHolder1_lblNameGrading").text
            SGPA = result.find(id="ctl00_ContentPlaceHolder1_lblSGPA").text
            CGPA  = result.find(id="ctl00_ContentPlaceHolder1_lblcgpa").text
            for i in range(1, len(_finaldata)):
                x = _finaldata[i].find_all('td')
                subject_data = x[0].text.split('-')
                subject_grade = x[3].text.rstrip()
                subject_code = str(subject_data[0]).rstrip()
                subject_type = subject_data[1].lstrip()
                subject = subject_code + subject_type
                result_data = {
                    'subject': subject,
                    'grade': subject_grade
                }
                _final_result.append(result_data)
            return ([name,SGPA,CGPA,_final_result])
        except:
            print('err')
            return "Error"
