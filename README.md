# Smart-Surveillance-System

## BASIC SETUP
![IMG_20190207_155957_HDR](https://user-images.githubusercontent.com/42694653/88503096-5268fe00-cfee-11ea-9f62-8036d6820fd5.jpg)


The goal of the project is to develop a low-cost remote surveillance system using Raspberry Pi platform that provides the user with a much better way for monitoring. As the user should not be bothered by a constant alert in case of any motion detected, it additionally performs an image processing on the images in the cloud and then sends an alert using a text message to the user.

In this prototype, the detection of the motion and capturing of the image is done on the Raspberry Pi and the image processing is done on the PC which acts as a local server. The basic working of the complete prototype can be described in the following steps:

## The Raspberry Pi’s functioning:
1. Sense motion using PIR sensor.
2. If motion is detected:
I. Capture images using the camera module.
II. Zip the folder that contain the images.
III. Send the zipped file to cloud (in this case Dropbox)
3. If motion not detected, repeat Step 1 after some interval of time.

The next time it detects motion, the previously captured images and zipped file are deleted, thus clearing up the space on Raspberry Pi.

### Flowchart : Pi 
![frpi](https://user-images.githubusercontent.com/42694653/88502512-4a0fc380-cfec-11ea-8544-420f736c4ff5.png)




## The program running on the server:

1. Check if new file has arrived in the Dropbox.

2. If new file is detected:

    I. Download the file.
  
    II. Unzip the file.
  
    III. Apply image processing on all the images.
  
    IV. Check if human detected.
  
      i. If yes, send a notification to the user.
    
      ii. Save a copy of the image.
    
    V. Delete the file from the Dropbox.
  
3. If new file is not detected, check the Dropbox again after some interval of time.

### Flowchart : Server
![imgflow](https://user-images.githubusercontent.com/42694653/88502614-98bd5d80-cfec-11ea-81f5-ef0243ec21a6.png)


## Experimental Result
The below images were captured by the camera attached to Raspberry Pi.
![image0](https://user-images.githubusercontent.com/42694653/88503031-0cac3580-cfee-11ea-92fc-c6be46918ca0.jpg)

![image1](https://user-images.githubusercontent.com/42694653/88503064-382f2000-cfee-11ea-8d24-8c3d6091ddad.jpg)

## Terminal view of Raspberry Pi
![TerminalRPI](https://user-images.githubusercontent.com/42694653/88503417-4893ca80-cfef-11ea-97b1-af08efbff2a4.PNG)


## Terminal view of Server Machine
![TerminalServer](https://user-images.githubusercontent.com/42694653/88503432-56e1e680-cfef-11ea-81a5-2b70d78006b2.png)


## Notification received on User's phone
![Screenshot_2019-02-07-17-31-22-101_com android mms](https://user-images.githubusercontent.com/42694653/88503626-e9828580-cfef-11ea-9094-b2486950d60f.png)


### Credit 
This project uses the source code from pyimage search with minor modification for the image processing task on the server side.
Feel free to follow the tutorial from the link below:

https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/

Suggestions are always welcomed. Raise an issue, if you got any.

Thank you!

~thevirtualbuddy
