#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:50:23 2019

@author: krishna
"""

import face_recognition
import numpy as np
import cv2
from vidstab import VidStab

video_capture_0 = cv2.VideoCapture(0)
video_capture_1 = cv2.VideoCapture(1)
#pavan_img = face_recognition.load_image_file("C:/Users/RAMBABU/Desktop/vineet.jpeg")
#pavan = face_recognition.face_encodings(pavan_img)[0]
akhil_img = face_recognition.load_image_file("/home/krishna/Desktop/hawkeye/akhil.jpeg")
akhil = face_recognition.face_encodings(akhil_img)[0]
known_face_encodings = [akhil]
known_face_names = ["akhil"]
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
stabilizer = VidStab(kp_method='FAST', threshold=42, nonmaxSuppression=False)


while True:
    # Capture frame-by-frame
    ret0, frame0 = video_capture_0.read()
    stabilized_frame = stabilizer.stabilize_frame(input_frame=frame0, border_size=50)
    small_frame = cv2.resize(stabilized_frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    for (top, right, bottom, left), name in zip(face_locations, face_names):

        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame0, (left, top), (right, bottom), (0, 0, 255), 2)


        cv2.rectangle(frame0, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame0, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    ret1, frame1 = video_capture_1.read()
    stabilized_frame = stabilizer.stabilize_frame(input_frame=frame1, border_size=50)
    small_frame = cv2.resize(stabilized_frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    for (top, right, bottom, left), name in zip(face_locations, face_names):

        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame1, (left, top), (right, bottom), (0, 0, 255), 2)


        cv2.rectangle(frame1, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame1, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    if (ret0):
        # Display the resulting frame
        cv2.imshow('Cam 0', frame0)

    if (ret1):
        # Display the resulting frame
        cv2.imshow('Cam 1', frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture_0.release()
video_capture_1.release()
cv2.destroyAllWindows()