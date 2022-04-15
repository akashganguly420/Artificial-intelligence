from  ..module.module import *

def olt():
     os.system('netsh interface ip set address name="Wi-Fi" static 192.168.8.12 255.255.255.0')

     time.sleep(5)
     webbrowser.open_new_tab("https://192.168.8.100")
     time.sleep(3)
     time.sleep(0.2)