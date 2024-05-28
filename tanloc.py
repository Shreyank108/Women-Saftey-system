from selenium import webdriver
import pywhatkit as py
import cv2 
import numpy as np 
from time import sleep
import pyautogui
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
url = "https://www.google.com/maps"
driver.get(url)
sleep(2)
driver.find_element("id", "sVuEFc").click()
sleep(2)
driver.current_url
print(driver.current_url)  
p=pyautogui.screenshot()
p=cv2.cvtColor(np.array(p),
                     cv2.COLOR_RGB2BGR)
   
cv2.imwrite("image1.png", p) 
py.sendwhats_image('+',p)