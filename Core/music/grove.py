from  ..module.ai import *

def grove():
    pyautogui.hotkey('win')
    time.sleep(0.5)
    pyautogui.write('Grove music')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.hotkey('space')
    time.sleep(0.5)
    akash = statement = takeCommand().lower()

    internal = 'play'

    if akash == internal:

        speak('gO bACK FOR SAY STOP')
        speak('say song name to play')

        while True:
            play = statement = takeCommand().lower()

            pyautogui.hotkey('ctrl', 'q')
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('del')
            pyautogui.write(play)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.press('enter')
    elif 'next' in statement:
        pyautogui.hotkey('ctrl', 'f')
    elif 'back' in statement:
        pyautogui.hotkey('ctrl', 'b')
    elif "stop" in statement:
        speak('back in step') 
        