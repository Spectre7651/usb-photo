# Usb-Photo
### A useful tool for taking pictures from the command line using a usb webcam on Raspberry Pi

#### How to install:
In the shell **```wget https://raw.githubusercontent.com/alfie-ford/usb-photo/main/install.sh```**
Then run the script and it will install the apps needed and configure the program to work. Once that has downloaded you can edit where the photos are saved in the usb-photo.py file and change the **```save_location = "/home/pi/Pictures"```** line to reflect your user/system.

#### Commands:
To take a photo either type **```usb-photo```** and answer the prompt or type **```usb-photo -f [filename]```** to take a photo
Please note that you **don't** need to add the *.jpg* at the end of the filename as the progam automatically adds it in.
#### Dependancies
The following programs/settings are required
* sudo permissions
* Python3
