import pyttsx3
import speech_recognition as sr
import datetime
from playsound import playsound
import wikipedia
import os
import webbrowser
import cv2
import random
from requests import get
# import pywhatkit
import pyjokes
import keyboard
import requests
import pyautogui
from pywikihow import search_wikihow
import psutil
from bs4 import BeautifulSoup
import wolframalpha
try:
    app = wolframalpha.Client("AETJH7-9A3J8LGAJH")                
except:
    speak("no data found") 

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en_in')
            print(f"User said: {query}\n")
        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"

        return query    

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")
    speak("Hello sir i am jarvis how may i help you")

def YoutubeAuto():
    speak("what can i do sir ?")
    cm = takecommand().lower()

    if"puasse" in cm:
        keyboard.press('space bar')

    elif"restart" in cm:
        keyboard.press('0')

    elif"mute" in cm:
        keyboard.press('m')

    elif"skip" in cm:
        keyboard.press('l')

    elif"back" in cm:
        keyboard.press('j')

    elif"full screen" in cm:
        keyboard.press('f')

    elif"file mode" in cm:
        keyboard.press('t')

    speak("done sir!")  

# def dicti():
#     import PyDictionary
#     speak("ok sir, tell me what you are serching for")
#     cm = takecommand().lower()
    
#     if "meaning" in cm:
#         cm = cm.replace("what is ","")
#         cm = cm.replace("tha ","")
#         cm = cm.replace("meaning","")
#         cm = cm.replace("of","")
#         results = PyDictionary.meaning(cm)
#         speak(f"the meaning of {cm} is {results}")
    
#     elif"synonym" in cm:
#         cm = cm.replace("what is the synonym of","")
#         results = PyDictionary.synonym(cm)
#         speak(f"the synonym of {cm} is {results}")  

def speedtest():
    import speedtest
    speak("ok sir, i am checking speed")     
    sp = speedtest.Speedtest()
    down = sp.download()
    correctDown = int(down/800000)
    up = sp.upload()
    correctUp = int(up/800000)

    if"uploading" in query:
        speak(f"the uploading speed is {correctUp} mbp s")
    elif"downloading" in query:
        speak(f"the downloading speed is {correctDown} mbp s")  
    elif"inter" in query:
        speak(f"the uploading speed is {correctUp} mbp s and the downloading speed is {correctDown} mbp s") 


def taskeccution():
    wish()
    while True:
        query = takecommand().lower()        

        if 'wikipedia' in query: 
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            speak("ok sir, what can i search")
            cm = takecommand().lower()
            webbrowser.open (f"https://www.youtube.com//results?search_query={cm}") 
            speak("done sir!")

        elif"youtube listen" in query:
            YoutubeAuto()                

        elif"close youtube" in query:
            os.system("TASKKILL /f /im chrome.exe") 
        
        elif "opne website" in query:
            speak("which website sir")
            cm = takecommand().lower()
            speak("ok sir, launching...")
            webbrowser.open (f"https://www.google.com/search?q={cm}")
            speak("sir it's done")    
        
        elif"close website" in query:
            os.system("TASKKILL /f /im chrome.exe")
 
        elif "search google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif"close google" in query:
            os.system("TASKKILL /f /im chrome.exe")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"Sir your ip address is {ip}")
                
        elif "whatsapp " in query:
            speak("ok sir, whats tha message ")
            cm = takecommand().lower()
            pywhatkit.sendwhatmsg("+916260074298",f"{cm}",17,44)

        elif "play music" in query:
            music_dir ="D:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            print(songs)   
            os.startfile(os.path.join(music_dir, rd))

        elif"close music" in query:
            os.system("TASKKILL /f /im groove music.exe")

        elif "song" in query:
            speak("ok sir, which song you want listen")
            song = takecommand().lower()
            pywhatkit.playonyt(song) 
            speak("sir! your song has been playing")

        elif"close song" in query:
            os.system("TASKKILL /f /im chrome.exe")        
        
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")

        elif "open vs code" in query:
            vscodepath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(vscodepath)

        elif"close vs code" in query:
            os.system("TASKKILL /f /im Code.exe")    

        elif "open illustrator" in query:
            illustratorspath = "C:\\Program Files\\Adobe\\Adobe Illustrator 2020\\Support Files\\Contents\\Windows\\Illustrator.exe"    
            os.startfile(illustratorspath)

        elif"close illustrator" in query:
            os.system("TASKKILL /f /im Illustrator.exe")    
        
        elif "open nfs" in query:
            nfspath = "E:\\Need for Speed Most Wanted\\NFS13.EXE"            
            os.startfile(nfspath)
        
        elif"close nfs" in query:
            os.system("TASKKILL /f /im NFS13.EXE")    
                
        elif "open photoshop" in query:
            photoshoppath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
            os.startfile(photoshoppath)

        elif"close photoshop" in query:
            os.system("TASKKILL /f /im Photoshop.exe") 

        elif "open chrome " in query:
            chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"           
            os.startfile(chromepath)

        elif"close chrome" in query:
            os.system("TASKKILL /f /im chrome.exe")  

        elif "open excel" in query:
            excelpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"            
            os.startfile(excelpath)

        elif"close excel" in query:
            os.system("TASKKILL /f /im EXCEL.EXE")    

        elif "open power point" in query:
            powerpointpah = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"            
            os.startfile(powerpointpah)

        elif"close power point" in query:
            os.system("TASKKILL /f /im POWERPNT.EXE")    

        elif "open word" in query: 
            wordpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"           
            os.startfile(wordpath)

        elif"close word" in query:
            os.system("TASKKILL /f /im WINWORD.EXE")    

        elif "open camera" in query:
            camera = cv2.VideoCapture(0)
            while True:
                ret, img = camera.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            camera.release()
            cv2.destroyAllWindows()

        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif"google search" in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google","")
            query = query.replace("search","")
            speak("ok sir! , wait a minute")
            speak("sir her what i found")
            pywhatkit.search(query)

            try:
                result= googleScrap.summary(query,3)
                print(result)
                speak(result)
            
            except:
                speak("no data is availablel") 

        elif"repeat me" in query:
            speak("ok sir!")
            cm = takecommand()
            speak(cm)

        elif "how to" in query:
            speak("feching to in data base!")
            cm = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(cm,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary) 

        elif"speed" in query:
            query = query.replace("jarvis","")
            query = query.replace("speed","")
            speedtest()

        elif"power" in query or "battery" in query:
            battery = psutil.sensors_battery()
            per = battery.percent
            speak(f"sir our system have {per} percentage power") 
            if per>=75:
                speak("sie we have enough power you can continue our work")
            elif per>=45 and per<75:
                speak("sir i think we should connect our system to charging point to charge battery")
            elif per>=15 and per<45:
                speak("sir dont't have enough power to work, please connect to charging")
            elif per<15:
                speak("sir we have very low power, please connect system to charging the system very soon")

        # elif "where i am" in query or "where we are" in query  or "location" in query:
        #         speak("wait sir, let me check")
        #         try:
        #             ip = get('https://api.ipify.org').text    
        #             print(ip)                   
        #             url = 'https://get.grojs.io/vl/ip/geo'+ip+'.json'
        #             geo_requests = requests.get(url)
        #             geo_data = geo_requests.json()
        #             city = geo_data('city')
        #             state = geo_data('state')
        #             country = geo_data('country')
        #             speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
        #         except:
        #             speak("sorry sir, due the network issue i am not able to find where we are")
        # elif"dictionary" in query:
        #     dicti()
            
        elif"screenshot" in query:
            speak("ok sir!, which name i should save this file ?")
            name = takecommand()
            speak("sir wait a second, i am taking screenshort")
            # time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir")

        elif "private" in query or "show my file" in query:
            speak("sir please tell me you want to hide all file or make visible to everyone")
            cm = takecommand().lower()

            if "private" in cm:
                os.system("attrib +h +s +r")

            elif"show" in cm:
                os.system("attrib -h -s -r") 

            elif"leave" in cm:
                speak("ok sir")            

        elif"weather" in query:
            try:
                re = app.query(query)
                print(next(re.results).text)
                speak("sir the curren weather")
                speak(next(re.results).text)
            except:
                url = f"https://www.google.com/search?q={query}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"sir the current weather at {query} is {temp}")

        elif"alarm" in query:
            speak("ok sir, please tell me the time")
            time = input("Enter the time")

            while True:
                time_At = datetime.datetime.now()
                now = time_At.strftime("%H:%M:%S")

                if now == time:
                    speak("Time to wake up sir")
                    playsound("iron man")
                    speak("Alarm Closed!")

                elif now>time:
                    break                

if __name__ == "__main__":
    
    import cv2 

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 2

    names = 'Himanshu'

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:
        ret, img = cam.read()

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
            )

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])

            if (accuracy < 57):
                id = names
                accuracy = "  {0}%".format(round(100 - accuracy))
                speak("success verified")
                taskeccution()

            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
                speak("wrong authentication")


            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,255), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break


    cam.release()
    cv2.destroyAllWindows()








        
                    


                        
                

            
    




        









