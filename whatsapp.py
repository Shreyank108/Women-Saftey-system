import pywhatkit
import gmap
import pyautogui as k 
pywhatkit.sendwhatmsg_instantly("+","hii i am good") 
p=pywhatkit.search("my current location")
k.press("enter")
pywhatkit.sendwhatmsg_instantly("+",p) 
gmap.GoogleMap()
