import cv2
from PIL import Image
from util import get_limits
#info de la webcam
cap = cv2.VideoCapture(1)

red = [40, 20, 150]
blue = [30, 20, 150]

while True:
    ret, frame = cap.read()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=red)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frameWithBbox = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        cv2.imshow("frame", frameWithBbox)
    else:
        cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break