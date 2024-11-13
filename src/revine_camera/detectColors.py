# imported our libraries and archives
import cv2
from PIL import Image
from util import get_limits
import numpy as np

# webcam info
cap = cv2.VideoCapture(0)


## DEFINITIONS

# detecting objects
def detect_object(frame, color):
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    cv2.imshow("frame", frame)  # shows the camera

    if bbox is not None:
        return bbox  # returns (x1, y1, x2, y2)
    return None

# analyze width and color of frames
def analyze_sides(frame):
    # converts the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # get the dimensions of the frame
    height, width = gray.shape
    
    # define the regions of interest (ROI) for left and right sides
    left_roi = gray[:, :width//2]
    right_roi = gray[:, width//2:]
    
    # calculate the average brightness of each ROI
    left_brightness = np.mean(left_roi)
    right_brightness = np.mean(right_roi)
    
    # cetermine which side is brighter (whiter)
    if left_brightness > right_brightness:
        return "left", left_brightness, right_brightness
    elif right_brightness > left_brightness:
        return "right", left_brightness, right_brightness
    else:
        return "equal", left_brightness, right_brightness
