from  ..module.ai import *

engine = pyttsx3.init()
words = ['hello', 'word']
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
		


        # speak("Tell me how can I help you now?")

	




def send():
    print('hello')
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                            cv2.COLOR_RGB2BGR)

    cv2.imwrite("mess.png", image)
    print('scr taken')

    while True:

        time.sleep(3)
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),
                                cv2.COLOR_RGB2BGR)

        cv2.imwrite("mess2.png", image)
        print('scr2 taken')

        hash0 = imagehash.average_hash(Image.open('mess.png'))
        hash1 = imagehash.average_hash(Image.open('mess2.png'))
        cutoff = 5  # maximum bits that could be different between the hashes.

        if hash0 - hash1 < cutoff:
            print('msg not comed')
            speak('msg not recived')
        
        else:
            image = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(image),
                                    cv2.COLOR_RGB2BGR)

            cv2.imwrite("mess.png", image)
            print('scr taken')
            cv2.imwrite("mess.png", image)
            time.sleep(0.5)
            im = Image.open('mess2.png').convert('L')
            im = im.crop((600, 820, 1920, 920))
            im.save('message.png')
            time.sleep(0.5)
            # read message
            img = cv2.imread('message.png')
            config = '-l eng --oem 1 --psm 3'

            pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract' \
                                                    '.exe '
            text = pytesseract.image_to_string(img, config=config)

            # print text
            text = text.split('\n')
            print(text)
            speak(text)
            time.sleep(2)

            
            
            speak('say your message')
            time.sleep(0.5)
            statement = takeCommand().lower()
            time.sleep(0.5)
            pyautogui.write(statement)
            time.sleep(0.5)
            pyautogui.press('enter')