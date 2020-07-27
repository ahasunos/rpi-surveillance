# import the necessary packages

import dropbox
from array import array
import zipfile
import time
import numpy as np
import argparse
from imutils import paths
import cv2
import requests


def mainfunction():
	dbx = dropbox.Dropbox('PROVIDE YOUR TOKEN HERE')

	while True:

		a = []
		#Checking for files on dropbox
		for entry in dbx.files_list_folder('').entries:
			print(entry.name)
			a.append(entry.name)

		if len(a) == 0:
			print("[!] No Files in the cloud")
			time.sleep(2)
			#continue

		else:
			with open("images.zip","wb") as f:
				metadata, res = dbx.files_download('/'+a[-1]+'')
				f.write(res.content)
			print("[+] Successfully downloaded from the dropbox")

			dbx.files_delete('/'+a[-1]+'')

			print("[+] Successfully deleted from the dropbox")

			image_zip = zipfile.ZipFile('/home/clone/iotRPi/images.zip')
			image_zip.extractall('/home/clone/iotRPi/images')
			image_zip.close()

			print("[+] Unzip Success")


			time.sleep(1)

			# construct the argument parse and parse the arguments
			ap = argparse.ArgumentParser()
			#ap.add_argument("-i", "--image", required=True,
			#	help="path to input image")

			ap.add_argument("-i", "--images", required=True, help="path to images directory")
			ap.add_argument("-p", "--prototxt", required=True,
				help="path to Caffe 'deploy' prototxt file")
			ap.add_argument("-m", "--model", required=True,
				help="path to Caffe pre-trained model")
			ap.add_argument("-c", "--confidence", type=float, default=0.2,
				help="minimum probability to filter weak detections")
			args = vars(ap.parse_args())

			# initialize the list of class labels MobileNet SSD was trained to
			# detect, then generate a set of bounding box colors for each class
			CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
				"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
				"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
				"sofa", "train", "tvmonitor"]
			COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

			# load our serialized model from disk
			print("[INFO] loading model...")
			net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

			# load the input image and construct an input blob for the image
			# by resizing to a fixed 300x300 pixels and then normalizing it
			# (note: normalization is done via the authors of the MobileNet SSD
			# implementation)

			# loop over the image paths
			imagePaths = list(paths.list_images(args["images"]))
			#imagePaths = list(paths.list_images(/images)
			
			for imagePath in imagePaths:
		
				image=cv2.imread(imagePath)
				(h, w)=image.shape[:2]
				blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

				# pass the blob through the network and obtain the detections and
				# predictions
				print("[INFO] computing object detections...")
				net.setInput(blob)
				detections = net.forward()

				# loop over the detections
				for i in np.arange(0, detections.shape[2]):
					# extract the confidence (i.e., probability) associated with the
					# prediction
					confidence = detections[0, 0, i, 2]

					# filter out weak detections by ensuring the `confidence` is
					# greater than the minimum confidence
					if confidence > args["confidence"]:
						# extract the index of the class label from the `detections`,
						# then compute the (x, y)-coordinates of the bounding box for
						# the object
						idx = int(detections[0, 0, i, 1])
						box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
						(startX, startY, endX, endY) = box.astype("int")

						# display the prediction
						label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
						res = format(CLASSES[idx])
						if res == 'person':
							print("Human Detected")
							#Sending an alert over text message using fast2sms 
							url = "https://www.fast2sms.com/dev/bulk"

							payload = "sender_id=FSTSMS&message=Alert! Intruder is detected&language=english&route=p&numbers=9436523998"

							headers = {

							'authorization': "PROVIDE YOUR TOKEN HERE",

							'Content-Type': "application/x-www-form-urlencoded",

							'Cache-Control': "no-cache",

							}

							response = requests.request("POST", url, data=payload, headers=headers)

							#print(response.text)
							print("Successfully informed!")
						print("[INFO] {}".format(label))
						
						#print(format(label))
						cv2.rectangle(image, (startX, startY), (endX, endY), COLORS[idx], 2)
						y = startY - 15 if startY - 15 > 15 else startY + 15
						cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

				time.sleep(1)

if __name__ == "__main__":
	mainfunction()

