#get weather by using openweathermap onecall api
import requests
import datetime

def epoch2date(epoch):
    return datetime.datetime.fromtimestamp(epoch).strftime('%d/%m/%Y %H:%M:%S')

#get week day from epoch
def get_week_day(epoch):
    haftanin_gunu = {"Monday": "Pazartesi", "Tuesday": "Salı", "Wednesday": "Çarşamba", "Thursday": "Perşembe", "Friday": "Cuma", "Saturday": "Cumartesi", "Sunday": "Pazar"}
    return haftanin_gunu.get(datetime.datetime.fromtimestamp(epoch).strftime('%A'))

def ay_evre_hesabi(evre):
    if evre == 0 or evre == 1:
        return "Yeni Ay"
    elif evre == 0.5:
        return "Dolunay"
    elif evre == 0.25:
        return "İlk Dördün"
    elif evre == 0.75:
        return "Son Dördün"
    elif (evre > 0 and evre < 0.25) or (evre > 0.75 and evre < 1):
        return "Hilal"
    elif (evre > 0.25 and evre < 0.5) or (evre > 0.5 and evre < 0.75):
        return "Şişkin Ay"
    else:
        return "Hatalı Evre"

def hava_durumu_yazdir(obje, simdiMi, bugunMu):
    print("\n*********************************************************\n")
    print("Hava durumu: " + obje['weather'][0]['description'])
    if simdiMi:
        print(epoch2date(obje['dt']) + " (Şu an)")
        print("Sıcaklık: " + str(obje['temp']) + "°C")
        print("Hissedilen: " + str(obje['feels_like']) + "°C")
    else:
        if bugunMu:
            print(epoch2date(obje['dt']) + " (Bugün)")
        else:
            print(epoch2date(obje['dt']) + " ("+ get_week_day(obje['dt']) + ")")
        print("Gündüz sıcaklık: " + str(obje['temp']['day']) + "°C")
        print("Gece sıcaklık: " + str(obje['temp']['night']) + "°C")
        print("Minimum sıcaklık: " + str(obje['temp']['min']) + "°C")
        print("Maksimum sıcaklık: " + str(obje['temp']['max']) + "°C")
        print("Gündüz hissedilen: " + str(obje['feels_like']['day']) + "°C")
        print("Gece hissedilen: " + str(obje['feels_like']['night']) + "°C")
        print("Ay evresi: " + ay_evre_hesabi(obje['moon_phase']))
        print("Yağış olasılığı: %" + str(obje['pop']))
    print("Rüzgar hızı: " + str(obje['wind_speed']) + " m/s")
    print("Rüzgar açısı: " + str(obje['wind_deg']) + "°")
    print("Nem: %" + str(obje['humidity']))
    print("Basınç: " + str(obje['pressure']) + " hPa")
    print("Gün doğumu: " + epoch2date(obje['sunrise']))
    print("Gün batımı: " + epoch2date(obje['sunset']))
    print("Bulut: %" + str(obje['clouds']))
    print("\n*********************************************************\n")

def get_weather(lat, lon, api_key):
    url = 'https://api.openweathermap.org/data/2.5/onecall'
    params = {
        'lat': lat,
        'lon': lon,
        'exclude': 'minutely,hourly',
        'units': 'metric',
        'lang': 'tr',
        'appid': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    hava_durumu_yazdir(data['current'], True, True)
    for i in data['daily']:
        if i == data['daily'][0]:
            hava_durumu_yazdir(i, False, True)
        else:
            hava_durumu_yazdir(i, False, False)
        
enlem = float(input('Enlem giriniz: '))
boylam = float(input('Boylam giriniz: '))
api_key = input('API key giriniz: ')
get_weather(enlem, boylam)