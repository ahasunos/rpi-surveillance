This program and utility files run on the server side and it helps to check if any files are on dropbox. If a file is detected it does the following:
1. Download the file.
2. Unzip it.
3. Perform image processing to check the presence of human.
4. If a human is detected, send an alert message to the owner using the fastsms api.

Before execution of the perform make the necessary changes as mentioned below:
1. Insert your dropbox token authentication token.
2. Insert your fastsms authentication token.

To execute the program use the following syntax:
python surveillance.py --images images --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel



Regards,
~thevirtualbuddy