# This is a demo of running face recognition on a Raspberry Pi.
# This program will print out the names of anyone it recognizes 
# to the console.
import face_recognition
from picamera2 import Picamera2, Preview
import numpy as np
import time
import cv2

# Get a reference to the Raspberry Pi camera.
camera = Picamera2()

# Load a sample picture and learn how to recognize it.
print("Loading known face image(s)")
me_image = face_recognition.load_image_file("images/me-scsu.png")
me_encoding = face_recognition.face_encodings(me_image)[0]

# Initialize some variables
face_locations = []
face_encodings = []
# camera.start()

while True:
    camera.start()
    print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    frame = camera.capture_array()
    frame_small = cv2.resize(frame, (640, 480))
    rgb_img = cv2.cvtColor(frame_small, cv2.COLOR_BGR2RGB)
    cv2.imshow('frame', rgb_img)

    # Find all the faces and face encodings in the current frame 
    # of video
    face_locations = face_recognition.face_locations(rgb_img)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(rgb_img, face_locations)

    # Loop over each face found in the frame to see if it's someone we know.
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces([me_encoding], face_encoding)
        name = "<Unknown Person>"

        if match[0]:
            name = "Imad"

        print("I see someone named {}!".format(name))
    time.sleep(0.5)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    
