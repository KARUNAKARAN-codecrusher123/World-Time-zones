import speech_recognition as sr
import pyttsx3
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pytz

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


blessey = 0

def talk(text):
    engine.say(text)
    engine.runAndWait()


if blessey == 0:
    talk('hello iam angel Weather app voice assistant')
    talk('My devloper Codecrusher KARAN')
    print('hello iam angel Weather app voice assistant')
    talk('what can i do for you people')
    print('what can i do for you people')

else:
    print('cant get it')


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.......')
            talk('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Angel' in command:
                command = command.replace('blessy', '')
                print(command)
    except:
        pass
    return command


def run_blessy():
    command = take_command()
    print(command)
    if 'weather' in command:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

            def weather(city):
                city = city.replace(" ", "+")
                res = requests.get(
                    f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
                    headers=headers)
                print("Searching...\n")
                talk("Searching...\n")
                soup = BeautifulSoup(res.text, 'html.parser')
                location = soup.select('#wob_loc')[0].getText().strip()
                time = soup.select('#wob_dts')[0].getText().strip()
                info = soup.select('#wob_dc')[0].getText().strip()
                weather = soup.select('#wob_tm')[0].getText().strip()
                print(location)
                talk(location)
                print(info)
                talk(info)
                print(time)
                talk(time)
                ab = (weather + "??C")
                talk(ab)
                print(ab)
            city1 = "coimbatore"
            talk(city1)
            city = city1 + " weather"
            weather(city)
            abc = ("Have a fabulous day people")
            talk(abc)
            print(abc)

    elif 'world time' in command:
        Country_Zones = ['America/New_York', 'Asia/Kolkata', 'Australia/Sydney',
                         'Canada/Atlantic', 'Brazil/East', 'Chile/EasterIsland', 'Cuba', 'Egypt',
                         'Europe/Amsterdam', 'Europe/Athens', 'Europe/Berlin', 'Europe/Istanbul',
                         'Europe/Jersey', 'Europe/London', 'Europe/Moscow', 'Europe/Paris',
                         'Europe/Rome', 'Hongkong', 'Iceland', 'Indian/Maldives', 'Iran',
                         'Israel', 'Japan', 'NZ', 'US/Alaska', 'US/Arizona', 'US/Central',
                         'US/East-Indiana']

        country_time_zones = []
        for country_time_zone in Country_Zones:
            country_time_zones.append(pytz.timezone(country_time_zone))
        for i in range(len(country_time_zones)):
            country_time = datetime.now(country_time_zones[i])
            print(f"The date of {Country_Zones[i]} is {country_time.strftime('%d-%m-%y')} and The time of {Country_Zones[i]} is {country_time.strftime('%H:%M:%S')}")
            talk(f"The date of {Country_Zones[i]} is {country_time.strftime('%d-%m-%y')} and The time of {Country_Zones[i]} is {country_time.strftime('%H:%M:%S')}")

    elif 'thank you' in command:
        talk('Thank you for using me gentleman or Wommen!!!!, if you need any other information related news,to make call,whatsapp msgs or to know about location kindly contact my parent Voice Assistance')
    else:
        talk('cant get it....please say it again')


while True:
    run_blessy()