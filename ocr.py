import os
import json
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './a.json'

def detect_text_uri(uri):
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    try:
        captcha = str(list(texts)[0].description)
        captcha = captcha.replace(" ","")
        return captcha
    except:
        return 'Error'
# (detect_text_uri('http://result.rgpv.ac.in/result/CaptchaImage.axd?guid=3664f1b6-9d76-4331-a435-900d819a88d5'))


