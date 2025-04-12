import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv 
import pywhatkit
freq = 44100
duration = 10
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
sd.wait()
write("recording0.wav", freq, recording)
wv.write("recording1.wav", recording, freq, sampwidth=2) 
pywhatkit.sendwhatmsg_instantly("+",'recording1.wav') 
