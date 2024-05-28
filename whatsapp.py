import pywhatkit
import gmap
import pyautogui as k 
pywhatkit.sendwhatmsg_instantly("+918964864762","hii i am good") 
p=pywhatkit.search("my current location")
k.press("enter")
pywhatkit.sendwhatmsg_instantly("+918964864762",p) 
gmap.GoogleMap()