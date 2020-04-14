import requests as r
import json
import pandas as pd

def requestData(payload):
    
    response = r.get('https://search-maps.yandex.ru/v1/', params=payload)
    if response.status_code != 200: 
        print(response.text)
    else:
        data = json.loads(response.text)
        return data
        
def createParams(category,centerPoint,bbox):
    
    params = {'text':category,
              'lang':'ru_RU',
             'll':centerPoint,
             'bbox':bbox,
             'apikey':'',
             'results':'500'}
    return params

