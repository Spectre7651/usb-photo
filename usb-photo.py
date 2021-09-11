import os
import sys
from datetime import datetime
from guizero import App, Text, Picture
save_location = "/home/pi/Pictures"
#Get the date
dtnow = datetime.now()
dt_fmtd = dtnow.strftime("%d.%m.%Y_%H:%M")

try:
    mode = sys.argv[1]
    if mode == "-f":
        filename = sys.argv[2]
    else:
        filename = dt_fmtd
except IndexError:
    filename = dt_fmtd

#Create the filename to save image to
savename = str(save_location) + "/" + str(filename) + ".jpg"
#Take the photo with fswebcam
os.system("fswebcam -q {}".format(savename)) #Take the photo using fswebcam


app = App(title="Usb_Photo Image") #Sets up a python gui to output the image
test = Text(app, text="{}".format(savename))
img = Picture(app, image="{}".format(savename))
app.display() #Display the output
