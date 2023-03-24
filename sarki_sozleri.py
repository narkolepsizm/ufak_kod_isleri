from selenium import webdriver
from googletrans import Translator

ceviri = Translator()

def get_lyrics(artist,song_title, cevir = False):
    #format artist and song title
    artist = artist.lower()
    song_title = song_title.lower()
    #url variable to store url location of lyrics
    url = 'https://genius.com/' + artist + '-' + song_title + '-lyrics'
    #replace spaces with '-' in url
    url = url.replace(' ', '-')
    url = url.replace("'", '')
    url = url.translate(str.maketrans("çğıöşü", "cgiosu"))
    lyrics = ""
    #use try to catch exceptions
    try:
        #opening browser
        driver = webdriver.Chrome("C:\Program Files\chromedriver\chromedriver.exe")
        #getting url
        driver.get(url)
        #getting element
        element = driver.find_elements_by_css_selector("div[data-lyrics-container='true']")
        #getting text
        if cevir:
            for i in element:
                lyrics = lyrics + i.text + "\n\n\n" + ceviri.translate(i.text, dest='tr').text
        else:
            for i in element:
                lyrics = lyrics + i.text
        #closing browser
        driver.close()
    #use except to catch exceptions
    except Exception as e:
        #print error and error message
        print(e)
        print("Error")
        return "Hata"
    #clear console
    #print("\n" * 100)
    return lyrics
"""sanatci = input("Lütfen sanatçının adını giriniz: ")
sarki_adi = input("Lütfen şarkı adını giriniz: ")
print(get_lyrics(sanatci,sarki_adi))"""