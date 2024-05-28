import numpy as np
import cv2
import pyautogui
import time 
import pywhatkit 
import random

pywhatkit.search("my current location ") 
random_time=random.randint(4, 6)
time.sleep(random_time)
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image),
					cv2.COLOR_RGB2BGR)

cv2.imwrite("loc.png", image)
pywhatkit.sendwhats_image('+','loc.png')