from urllib.request import urlretrieve
import os
import requests
def getCaptcha(url):
    try:
        urlretrieve(str(url),'out.png')
        r =requests.post("https://secret-harbor.herokuapp.com/process",files={
            'file':open("out.png","rb")
        },data={
            'lang':'eng'
        }).json()
        os.remove("out.png")
        return str(r['ocr']['0']).replace(" ","")
    except:
        try:

            os.remove("out.png")
        except:
            return "Error"
        return "Error"
# print(getCaptcha('http://result.rgpv.ac.in/result/CaptchaImage.axd?guid=3742f6b2-2255-43a1-80c4-dedf58634166'))
# getCaptcha("http://result.rgpv.ac.in/Result/CaptchaImage.axd?guid=256a10ff-3b18-40eb-8ccc-f7ad6751aac4")