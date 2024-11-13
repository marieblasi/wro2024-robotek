import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]])   # BGR
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    hue = hsvC[0][0][0]
    lowerLimit = np.array([hue - 10, 100, 100])
    upperLimit = np.array([hue + 10, 255, 255])
    return lowerLimit, upperLimit
