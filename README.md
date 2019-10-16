# facenet-face-recognition

This repository contains a demonstration of face recognition using the FaceNet network (https://arxiv.org/pdf/1503.03832.pdf) and a webcam. Our implementation feeds frames from the webcam to the network to determine whether or not the frame contains an individual we recognize.

## How to use

To install all the requirements for the project run

	pip install -r requirements.txt

In the root directory. After the modules have been installed you can run the project by using python

	python facenet.py
	
The script will chech its database from /images folder

## NOTE

To fetch photos from openldap, set the uname and pw, and run

	python fetchphoto.py
	
This will automatically saves the photos in /images folder


Change the camera input depends on your primary or secondary camera (if you only got 1 camera input, set to 0)
```
camera = cv2.VideoCapture(1) #for secondary camera
camera = cv2.VideoCapture(0) #for primary camera
```
