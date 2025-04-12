#     - -  S - H - R - E - Y- A- N- K - - - - - - - - 

import speech_recognition as src 
import pyttsx3 
import pywhatkit  
from cv2 import VideoCapture, imwrite
cam=VideoCapture(0)
import numpy as np
import cv2 
import pyautogui 
import time 
import random 
                     
listner=src.Recognizer() 
engine=pyttsx3.init() 
voices=engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
 


def talk(text): 
    engine.say(text) 
    engine.runAndWait()
    
def command_taker(): 
        try: 
            with src.Microphone() as source : 
                print("i am listining")
                voice=listner.listen(source) 
                command =listner.recognize_google(voice) 
                command=command.lower() 
                if 'Help' or 'koi hai' or 'bachaao' or "Aaaaaaaa" in command : 
                    print (command) 
                command=command.replace('Help'or'koi hai'or'bachaao'or'Aaaaaaaa','')
        except Exception as e : 
            pass
        return command 
    
def run(): 
    command =command_taker() 
    p=f"i am in trouble ! i need help plz call police ! dial {100} "
    if 'help' or 'bachaao' or 'koi hai' or 'Aaaaaaaa' in command : 
        pywhatkit.sendwhatmsg_instantly("+9",f"{p}") 
        pyautogui.press("enter") 
        cam=VideoCapture(0)
        result,image=cam.read()
        if result:
            imwrite("image.png",image)
            pywhatkit.sendwhats_image("+9",'image.png')
        time.sleep(5)   
        pywhatkit.search("my current location ") 
        random_time=random.randint(4, 6)
        time.sleep(random_time)
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),
                            cv2.COLOR_RGB2BGR) 
        cv2.imwrite("loc.png", image)
        pywhatkit.sendwhats_image('+9******72','loc.png') 
                       
    else: 
        talk(" didnt rec sir plz try again by calling my name   ") 
    
    
run() 
