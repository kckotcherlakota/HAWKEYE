#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:10:55 2019

@author: krishna
"""


import face_recognition
import cv2
import numpy as np
from vidstab import VidStab
#def same(ret,frame):
#    ret, frame = video_capture.read()
#   
#    stabilized_frame = stabilizer.stabilize_frame(input_frame=frame, border_size=50) 
#    small_frame = cv2.resize(stabilized_frame, (0, 0), fx=0.25, fy=0.25)
#    rgb_small_frame = small_frame[:, :, ::-1]
#    if process_this_frame:
#
#        face_locations = face_recognition.face_locations(rgb_small_frame)
#        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
#
#        face_names = []
#        for face_encoding in face_encodings:
#
#            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#            name = "Unknown"
#            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#            best_match_index = np.argmin(face_distances)
#            if matches[best_match_index]:
#                name = known_face_names[best_match_index]
#
#            face_names.append(name)
#
#    process_this_frame = not process_this_frame
#
#
#    for (top, right, bottom, left), name in zip(face_locations, face_names):
#
#        top *= 4
#        right *= 4
#        bottom *= 4
#        left *= 4
#
#
#        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#
#
#        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#        font = cv2.FONT_HERSHEY_DUPLEX
#        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
#
#
#    cv2.imshow('Video', frame)


video_capture = cv2.VideoCapture(0)
pavan_img = face_recognition.load_image_file("vineet.jpeg")
pavan = face_recognition.face_encodings(pavan_img)[0]
akhil_img = face_recognition.load_image_file("akhil.jpeg")
akhil = face_recognition.face_encodings(akhil_img)[0]
#sahithya_img = face_recognition.load_image_file("sahithya.jpeg")
#sahithya = face_recognition.face_encodings(sahithya_img)[0]
known_face_encodings = [pavan, akhil]
known_face_names = ["vineet","akhil"]
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
stabilizer = VidStab(kp_method='FAST', threshold=42, nonmaxSuppression=False)

frame0 = cv2.VideoCapture(0)
frame1 = cv2.VideoCapture(1)
while 1:
   ret0, img1 = frame0.read()
   ret1, img2 = frame1.read()
#   img1 = cv2.resize(img0,(360,240))
#   img2 = cv2.resize(img00,(360,240))
   if (frame0):
       cv2.imshow('img1',img1)
       ret0, img1 = frame0.read()
       stabilized_frame = stabilizer.stabilize_frame(input_frame=img1, border_size=50) 
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
           cv2.rectangle(img1, (left, top), (right, bottom), (0, 0, 255), 2)
           cv2.rectangle(img1, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
           font = cv2.FONT_HERSHEY_DUPLEX
           cv2.putText(img1, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
       cv2.imshow('Video', img1)
   if (frame1):
       cv2.imshow('img1',img2)
       ret1, img2 = frame1.read()
       stabilized_frame = stabilizer.stabilize_frame(input_frame=img2, border_size=50) 
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
           cv2.rectangle(img2, (left, top), (right, bottom), (0, 0, 255), 2)
           cv2.rectangle(img2, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
           font = cv2.FONT_HERSHEY_DUPLEX
           cv2.putText(img2, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
       cv2.imshow('Video', img2)
       k = cv2.waitKey(30) & 0xff

   if k == 27:
      break
frame0.release()
frame1.release()
cv2.destroyAllWindows()