import sounddevice
import time
from scipy.io.wavfile import write  
import pywhatkit


def savefile(sec):
  i=1
  while i<5:
    print("start")
    rece=sounddevice.rec((sec*44100),samplerate=44100,channels=2)
    print("rec")
    sounddevice.wait()
    write(f"demo{i}.mp3",44100,rece)
    
    t=30
    while t>0:
     mins, secs = divmod(t, 60)
     timer = '{:02d}:{:02d}'.format(mins, secs)
     print(timer, end="\r")
     time.sleep(1)
     t -= 1
    i=i+1
    #.................................   
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with the path to your ChromeDriver executable
driver_path = '/path/to/chromedriver'

# Initialize ChromeDriver
driver = webdriver.Chrome(driver_path)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for the user to scan the QR code and log in
# Add additional delay if needed
wait = WebDriverWait(driver, 30).until(EC.title_contains('WhatsApp'))

# Replace 'contact_name' with the name of the contact you want to send the audio to
contact_name = '+918964864762'

# Find and click on the contact
contact_xpath = f'//span[@title="{contact_name}"]'
contact = wait.until(EC.presence_of_element_located((By.XPATH, contact_xpath)))
contact.click()

# Replace 'audio_path' with the path to your audio file
audio_path = 'demo1.mp3'

# Find and click on the attachment button
attachment_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@title="Attach"]')))
attachment_btn.click()

# Select the 'Document' option
document_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@accept="*"]')))
document_btn.send_keys(audio_path)

# Wait for the attachment to be uploaded
wait.until(EC.presence_of_element_located((By.XPATH, '//span[@data-testid="send"]')))

# Click on the send button
send_btn = driver.find_element(By.XPATH, '//span[@data-testid="send"]')
send_btn.click()

# Close the browser
driver.quit()

     
        
print("end")
savefile(10)    
    