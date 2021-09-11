#!/bin/bash

echo "Usb-Photo Setup Routine"

echo "Press Enter to Install The Program And Its Dependancies"

read enter #this just waits for the user to press enter to start the script

echo "Installing fswebcam"
$(sudo apt-get install fswebcam -y)

whoami=$(whoami)

echo "Adding $whoami to the video group"
$(sudo usermod -a -G video $whoami)

echo "Installing guizero via pip3"
$(sudo pip3 install guizero)

echo "Cloning the usb-webcam github repo"
$(git clone https://github.com/alfie-ford/usb-photo.git ~/)

echo "Setting up the prompt"
$(sudo cp  ~/usb-photo/usb-photo /usr/bin/)


