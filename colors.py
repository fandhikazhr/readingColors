import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 100, 100], np.uint8) # setting the blue lower limit
    upper_blue = np.array([120, 255, 255], np.uint8) # setting the blue upper limit
    blue = cv2.inRange(hsv, lower_blue, upper_blue)

    cnts1 = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts1 = imutils.grab_contours(cnts1)
