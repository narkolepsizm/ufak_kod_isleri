#find the cheapest flight from Istanbul to any destination in any time using skyscanner API 

import requests
import schedule
import time
from datetime import datetime, timedelta

def ucus_kontrol():
    ucus_bilgileri = {
        "country": "tr",
        "currency": "TRY",
        "locale": "tr-TR",
        "originplace": "ISTA-sky",
        "destinationplace": "CGN-sky",
        "outbounddate": "anytime",
        "inbounddate": "anytime",
        "adults": 1,
        "children": 0,
        "infants": 0,
        "cabinclass": "economy",
        "groupPricing": "true"
    }
    ucus_sonuc = requests.get('http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/TR/TRY/tr-TR/ISTA-sky/CGN-sky/anytime/anytime?apiKey=prtl6749387986743898559646983194', params = ucus_bilgileri)
    ucus_sonuc = ucus_sonuc.json()
    print(ucus_sonuc)
    #save the cheapest flight to a file
    with open("ucusbul.json", "w") as ucusbul:
        ucusbul.write(str(ucus_sonuc))
    """ucus_sonuc = ucus_sonuc["Quotes"]
    ucus_sonuc = sorted(ucus_sonuc, key = lambda i: i['MinPrice'])
    ucus_sonuc = ucus_sonuc[0]
    ucus_sonuc = ucus_sonuc["MinPrice"]
    print(ucus_sonuc)
    if(ucus_sonuc < 1000):
        print("Ucuz ucus bulundu: "+"Ucuz ucus bulundu. Fiyat: "+str(ucus_sonuc))
    else:
        print("Ucuz ucus bulunamadi")"""

ucus_kontrol()
