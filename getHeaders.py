import requests
from bs4 import BeautifulSoup
def getHeaders():
    html= requests.get("http://result.rgpv.ac.in/Result/ProgramSelect.aspx").text
    soup = BeautifulSoup(html,'html.parser')
    __VIEWSTATE  =soup.find(id ="__VIEWSTATE").get('value'),
    __EVENTVALIDATION = soup.find(id ="__EVENTVALIDATION").get('value')
    return ([__VIEWSTATE,__EVENTVALIDATION])
