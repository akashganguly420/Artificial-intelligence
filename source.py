
#created Modules
from Core.Objects.utube            import *
from Core.Objects.whatsapp         import *
from Core.Objects.mail             import *
from Core.Objects.send             import *
from Core.Objects.write            import *
from Core.windows.boot             import *
from Core.windows.battery          import *
from Core.windows.tele             import *
from Core.windows.akash            import *
from Core.windows.scan             import *
from Core.windows.write            import *
from Core.hack.android             import *
from Core.hack.windows             import *
from Core.wsl.route                import *
from Core.network.olt              import *
from Core.music.grove              import *


#The ai code
from Core.module.ai                import *



#speak diffen on time
def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
wishMe()

speak('sam online')








	

if __name__ == '__main__':

    while True:
        

        statement = takeCommand().lower()
        if statement == 0:
            continue
        #Hello is the command for accesss all commands
        if 'hello' in statement:
            speak("Hii Sir")

            #time only 5 second
            for x  in statement:
                print(x)

            
               
                
                #command starting here
                statement = takeCommand().lower()
                if statement == 0:
                    continue
                elif 'how are you' in statement:
                    speak('i am fine')                                 

                               

                elif 'start server android' in statement:
                    android()
                    speak('server is opening')
                    
                elif 'start server windows' in statement:
                    windows()
                    speak('server is starting')                    
                
                elif 'boot windows' in statement:
                    boot()

                elif 'open my mail' in statement:
                    mail()
                elif 'youtube' in statement:
                   utube()              

                elif 'open whatsapp' in statement:
                    whatsapp()                  
                    
                elif 'send' in statement:
                    send()                 

                elif 'check battery' in statement:
                    battery()                   

                    
                elif 'minimise all applications' in statement:
                    pyautogui.hotkey('win', 'd')
                    speak("minimized")

                elif 'maximize all applications' in statement:
                    pyautogui.hotkey('win', 'd')
                    speak('maximized')

                elif 'next' in statement:

                    pyautogui.press('tab')

                elif 'call my phone' in statement:
                    os.system('Recording.mp3')
                elif 'nice' in statement:
                    speak('thank uou sir')
                    
                elif 'route my network' in statement:
                    route()
                    speak('please enter port and ip')

                elif 'telegram' in statement:
                    tele()                   

                    
                elif 'call akash' in statement:
                    akash()

                elif 'write mode' in statement:
                    write()                        

                elif 'open switch' in statement:
                    olt()
                    speak('please fill login Data')

                elif 'scan' in statement:
                    scan()                

                elif 'play music' in statement:
                    grove()
                #write commands
                elif 'write' in statement:
                    likh()
                    speak('code executed')

                

                        
                



    
                                



