#requirements
#async-generator==1.10
#attrs==22.1.0
#beautifulsoup4==4.11.1
#certifi==2022.9.24
#charset-normalizer==2.1.1
#exceptiongroup==1.0.1
#h11==0.14.0
#idna==3.4
#outcome==1.2.0
#packaging==21.3
#pydub==0.25.1
#pyparsing==3.0.9
#PySocks==1.7.1
#python-dotenv==0.21.0
#requests==2.28.1
#selenium==4.6.0
#sniffio==1.3.0
#sortedcontainers==2.4.0
#soupsieve==2.3.2.post1
#SpeechRecognition==3.8.1
#tqdm==4.64.1
#trio==0.22.0
#trio-websocket==0.9.2
#urllib3==1.26.12
#webdriver-manager==3.8.4
#wsproto==1.2.0

#add-on-requirements
#sudo apt install ffmpeg

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import speech_recognition as sr
from bs4 import BeautifulSoup
from pydub import AudioSegment
import os, sys
from os import path
import time,requests

delayTime = 2
audioToTextDelay = 10

filename = 'audio.mp3'
byPassUrl = 'https://www.google.com/recaptcha/api2/demo'

brave_path = '/usr/bin/brave-browser-stable'
option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")

def audioToText(mp3Path):
    input_file = mp3Path
    output_file = "result.wav"

    sound = AudioSegment.from_mp3(input_file)
    sound.export(output_file, format="wav")

    r = sr.Recognizer()
    with sr.AudioFile("result.wav") as source:
        audio = r.record(source)

    try:
        s = r.recognize_google(audio)
        return s
    except Exception as e:
        print(e)

def saveFile(content, filename):
    with open(filename, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)

driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='106.0.5249.61').install()), options=option)
driver.get(byPassUrl)

time.sleep(1)
googleClass = driver.find_elements(By.CLASS_NAME, 'g-recaptcha')[0]
time.sleep(2)
outeriframe = googleClass.find_element(By.TAG_NAME, 'iframe')
time.sleep(1)
outeriframe.click()
time.sleep(2)
allIframesLen = driver.find_elements(By.TAG_NAME, 'iframe')
time.sleep(1)

audioBtnFound = False
audioBtnIndex = -1

for index in range(len(allIframesLen)):
    driver.switch_to.default_content()
    iframe = driver.find_elements(By.TAG_NAME, 'iframe')[index]
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(delayTime)

    try:
        audioBtn = driver.find_element(By.ID, 'recaptcha-audio-button') or driver.find_element(By.ID, 'recaptcha-anchor')
        audioBtn.click()
        audioBtnFound = True
        audioBtnIndex = index
        break
    except Exception as e:
        pass

if audioBtnFound:
    try:
        while True:
            href = driver.find_element(By.ID, 'audio-source').get_attribute('src')
            response = requests.get(href, stream=True)
            saveFile(response,filename)
            response = audioToText(os.getcwd() + '/' + filename)
            driver.switch_to.default_content()
            iframe = driver.find_elements(By.TAG_NAME, 'iframe')[audioBtnIndex]
            driver.switch_to.frame(iframe)
            inputbtn = driver.find_element(By.ID, 'audio-response')
            inputbtn.send_keys(response)
            inputbtn.send_keys(Keys.ENTER)
            time.sleep(2)
            errorMsg = driver.find_elements(By.CLASS_NAME, 'rc-audiochallenge-error-message')[0]

            if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                print("Successessfully Verified !!!")
                break
    except Exception as e:
        print(e)
else:
    print('Successfully Verified without Audio !!!')
