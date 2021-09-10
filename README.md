# Usb-Photo
### A useful tool for taking pictures from the command line using a usb webcam on Raspberry Pi

#### How to install:
In the shell ```wget https://raw.githubusercontent.com/alfie-ford/usb-photo/main/install.sh```
This will install the apps needed and configure the program to work. Once that has downloaded you can edit where the photos are saved in the usb-photo.py file and change the ```save_location = "/home/pi/Pictures"``` line to reflect your user/system.

After that you can type: ```usb-photo``` in the terminal and a photo will be taken and stored in your prefered location
#### Dependancies
The following programs/settings are required
* sudo permissions
* Python3
* guizero - Python3
