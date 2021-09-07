import os
from datetime import datetime
from guizero import App, Text, Picture
save_location = "/home/pi/Pictures" # where the photo is saved (Change this to suit your system)
#Get the date
dtnow = datetime.now()
dt_fmtd = dtnow.strftime("%d.%m.%Y_%H:%M")


#Create the filename to save image to
filename = save_location + "/" + dt_fmtd +".jpg"

#Take the photo with fswebcam
os.system("fswebcam -q {}".format(filename)) #Take the photo using fswebcam


app = App(title="Usb_Photo Image") #Sets up a python gui to output the image
test = Text(app, text="{}".format(filename))
img = Picture(app, image="{}".format(filename))
app.display() #Display the output
