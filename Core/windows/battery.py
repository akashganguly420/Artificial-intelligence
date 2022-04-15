
from  ..module.module import *

engine = pyttsx3.init()
words = ['hello', 'word']
engine.say(random.choice(words))
newVoiceRate = 145
engine.setProperty('rate', newVoiceRate)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def battery():
    battery = psutil.sensors_battery()
    speak(battery.percent)
    speak("percentage")