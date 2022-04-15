from  ..module.module import *





engine = pyttsx3.init()
words = ['']
engine.say(random.choice(words))
newVoiceRate = 145
engine.setProperty('rate', newVoiceRate)


def speak(text):
    engine.say(text)
    engine.runAndWait()

	










def takeCommand():
    time.sleep(0.5)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=3)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            # speak("Pardon me, please say that again")
            return ""
        return statement




