from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
import webbrowser
import requests


r = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio=r.listen(source)
        voice=""
        try:
            voice=r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            print("Sizi Anlayamadım"),speak("Sizi Anlayamadım")
        except sr.RequestError:
            print("Sistem Çalışmıyor"),speak("Sistem Çalışmıyor")
        return voice



def rvr(voice):
    if "rvr asistan" in voice:
        print("Nasıl Yardımcı Olabilirim..."), speak("Nasıl Yardımcı Olabilirim")
        uyandirma = record()
        if uyandirma != '':
            print(voice.capitalize())
            response(voice)

def speak(string):
    tts=gTTS(text=string,lang="tr",slow=False)
    file="answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)




def start_app(app_name):
    if app_name == "uygulama aç":
        speak("Hangi uygulamayı açmamı istersin")
        return

    if not app_name:
        speak("Lütfen bir uygulama adı söyleyin")
        return
    try:
        app_path = os.path.join(os.path.expanduser("~"), r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs", app_name)
        if not os.path.exists(app_path):
            app_path = os.path.join(os.path.expanduser("~"), r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs", app_name)
        os.startfile(app_path)
        speak("İstediğin uygulamayı çalıştırıyorum")
    except FileNotFoundError:
        speak("Bu uygulama bulunamadı")

def response(voice):

        if "adın ne" in voice or "ismin ne" in voice:
            selection = ["Adım", "İsmim"]
            selection = random.choice(selection)
            speak(selection+"RVR Asistan")
        if "merhaba" in voice:
            speak("sizede merhaba")
        if "selam" in voice:
            speak("sizede selam")
        if "teşekkür ederim" in voice or "teşekkürler" in voice:
            speak("rica ederim")
        if "nasılsın" in voice or "iyi misin" in voice:
            speak("iyiyim siz nasılsınız")
        if "iyiyim ben de" in voice or "iyiyim" in voice:
            speak("iyi olmana sevindim")
        if "kötüyüm" in voice or "iyi değilim" in voice or "çok kötüyüm" in voice or "hiç iyi değilim" in voice:
            speak("üzülme herşey yoluna giricektir ben yanındayım")
        if "görüşürüz" in voice or "kapan" in voice or "çıkış yap" in voice or "uygulamayı kapat" in voice or "uygulamadan çık" in voice:
            selection = ["Elveda", "Görüşürüz","Gittiğine üzüldüm","Görüşmek üzere","baybay"]
            selection = random.choice(selection)
            speak(selection)
            exit()
        if "uygulama aç" in voice or "dosya aç" in voice:
            speak("Hangi uygulamayı açmamı istersin")
            app_name = record().lower()
            start_app(app_name)
        if "hangi gündeyiz" in voice or "günlerden ne" in voice or "bu gün günlerden ne" in voice:
            today=time.strftime("%A")
            today.capitalize()
            if today=="Monday":
                today="Pazartesi"

            elif today=="Tuesday":
                today="Salı"

            elif today=="Wednesday":
                today="Çarşamba"


            elif today=="Thursday":
                today="Perşembe"


            elif today=="Friday":
                today="Cuma"

            elif today=="Saturday":
                today="Cumartesi"

            elif today=="Sunday":
                today="Pazar"

            speak(today)
        if "saat kaç" in voice:
            selection=["Saat şu an: ","Hemen bakıyorum: "]
            clock=datetime.now().strftime("%H:%M")
            selection=random.choice(selection)
            speak(selection+clock)

        def hava_durumlarini_turkcelestir(hava_durumu):

            hava_durumlari = {
                "Clear": "Açık",
                "Clouds": "Bulutlu",
                "Rain": "Yağmurlu",
                "Snow": "Karlı",
                "Mist": "Sisli",
                "Thunderstorm": "Gök Gürültülü Sağanak Yağışlı",
                "Drizzle": "Çiy",
                "Haze": "Kırağı",
                "Partly cloudy": "Parçalı bulutlu"
            }

            return hava_durumlari[hava_durumu]

        if "hava" in voice or "bu gün hava nasıl" in voice or "hava durumu" in voice:

            print("Hangi şehrin hava durumunu merak ediyorsunuz?")
            speak("Hangi şehrin hava durumunu merak ediyorsunuz?")
            city_name = record()
            api_key = "YOUR API KEY !!!"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name

            response = requests.get(complete_url)

            if response.status_code == 200:
                data = response.json()

                main = data['main']

                sicaklik = main['temp']

                nem = main['humidity']

                basinc = main['pressure']

                fahrenheit = float(sicaklik)
                celsius = round(fahrenheit - 273)

                # hPa = float(pressure)
                # psi = (hPa * 0.0145038)

                detay = data['weather']

                print(f"{city_name:}")
                print(f"Sıcaklık: {celsius}°C")
                print(f"Nem: %{nem}")
                print(f"Basınç: {basinc}")
                print(f"Hava: {hava_durumlarini_turkcelestir(detay[0]['main'])}")
                speak(city_name+" için Hava durumu şu şekilde:")
                speak(f"Sıcaklık: {celsius}°C")
                speak(f"Nem: %{nem}")
                speak(f"Basınç: {basinc}")
                speak(f"Hava: {hava_durumlarini_turkcelestir(detay[0]['main'])}")





        if "google aç" in voice or "arama yap" in voice:
            speak("Ne aramamı istersin")
            search=record()
            url="https://www.google.com/search?q={}".format(search)
            webbrowser.get().open(url)
            speak("{} için Google'da bulabildiklerimi listeliyorum.".format(search))

        if "youtube aç" in voice:
            speak("Ne açmamı istersin")
            search = record()
            url = "https://www.youtube.com/results?search_query={}".format(search)
            webbrowser.get().open(url)
            speak("{} Youtube'u açıyorum.".format(search))

        if "not et" in voice:
            speak("Dosya ismi ne olsun?")
            txtFile=record()+".txt"
            speak("Ne kaydetmek istiyorsun")
            theText=record()
            f=open(txtFile,"w",encoding="utf-8")
            f.writelines(theText)
            f.close()
            print("Kayıt başaralı uygulamayı kapattıktan sonra dosya oluşturulacaktır"),speak("Kayıt başaralı uygulamayı kapattıktan sonra dosya oluşturulacaktır")
        print("Sizi Dinliyorum..."), speak("Sizi Dinliyorum...")

print("Sizi Dinliyorum..."),speak("Sizi Dinliyorum...")

while True:
    voice=record()
    if voice!='':
        voice=voice.lower()
        print(voice.capitalize())
        response(voice)







