import time
import RPi.GPIO as GPIO
from time import sleep
import os
import dropbox
import zipfile

from picamera import PiCamera
import picamera

def mainfunc():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21,GPIO.IN) #Replace 21 with the input pin you use in the Raspberry Pi GPIO
    
    counter = 0
    zipnum = 1
    camera = PiCamera()
    
    try:
        while True:
                input=GPIO.input(21)
                
                if input==0:
                    print("Looking for Intruder: " + str(counter))
                    counter = counter + 1
                    time.sleep(1)
                
                elif input==1:
                    print("Intruder detected, shoo them away!")
                    
                    camera.start_preview()
                    
                    for i in range(2):
                        sleep(1)
                        camera.capture('/home/pi/Desktop/SmartSurveillance/Captured/image%s.jpg' % i) #Here replace with the path with your own path where the file would be present
                    
                    camera.stop_preview()
                    time.sleep(1)

                    #This part of the code is zipping the images that are stored in a folder called testImage.
                    def zipdir(path,ziph):
                        for root, dirs, files in os.walk(path):
                            for file in files:
                                ziph.write(os.path.join(root,file))
                    zipf = zipfile.ZipFile('Zipped_file.zip','w',zipfile.ZIP_DEFLATED)
                    zipdir('./testImage',zipf)
                    zipf.close()
                    print("Successfully Zipped")

                    #This part of the code is sending the file to dropbox
                    f = open('/home/pi/Desktop/SmartSurveillance/Zipped_file.zip') #Here replace with the path with your own path where the file would be present
                    dbx = dropbox.Dropbox('PROVIDE YOUR TOKEN HERE') 
                    dbx.files_upload(f.read(),'/motionsenseCamPi%s.zip'%zipnum)
                    zipnum = zipnum + 1
                    print("Successfully uploaded to Cloud!")
                    f.close()
                    time.sleep(2)



    finally:
            GPIO.cleanup()



if __name__ == "__main__":
    mainfunc()

