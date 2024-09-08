from motor import forward, backwards, stop, left, right
from ser import read_sensors
from time import sleep, time
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Constants
FORWARD_SPEED = 1.0
FORWARD_TIME = 0.3
BACKWARD_SPEED = 1.0
BACKWARD_TIME = 0.3
STOP_TIME = 0.05

# Color thresholds in HSV for red and green
RED_LOWER = np.array([0, 100, 100])
RED_UPPER = np.array([10, 255, 255])

GREEN_LOWER = np.array([60, 100, 100])
GREEN_UPPER = np.array([80, 255, 255])

# Detect block colors and return the color detected ('red', 'green', or None)
def detect_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mask for red and green 
    mask_red = cv2.inRange(hsv, RED_LOWER, RED_UPPER)
    mask_green = cv2.inRange(hsv, GREEN_LOWER, GREEN_UPPER)

    # Find the number of non-zero pixels (i.e., the number of pixels that match the color)
    red_count = cv2.countNonZero(mask_red)
    green_count = cv2.countNonZero(mask_green)

    if red_count > 5000:  # Adjust threshold based on testing
        return 'red'
    elif green_count > 5000:  # Adjust threshold based on testing
        return 'green'
    else:
        return None

def handle_color_detection(color_detected):
    if color_detected == 'red':
        print("Red block detected. Going around to the right.")
        # Maneuver around the red block (right turn)
        right(300)
        forwardtime()
        left(300)
        forwardtime()
    elif color_detected == 'green':
        print("Green block detected. Going around to the left.")
        # Maneuver around the green block (left turn)
        left(300)
        forwardtime()
        right(300)
        forwardtime()

def main_loop():
    while True:
        ret, frame = cap.read()
        sensor_values = read_sensors()
        
        if sensor_values:
            dist_l, dist_t, dist_r, qtr_L, qtr_R = sensor_values
            print(f"Distances -> Left: {dist_l}, Front: {dist_t}, Right: {dist_r}")

            # Check for color detection
            color_detected = detect_color(frame)
            if color_detected:
                # Handle color detection (red or green block)
                handle_color_detection(color_detected)
                continue  # Skip sensor-based movement if a color block was detected

            # Move the robot forward if no block is detected and there are no obstacles
            if dist_t > 65 and dist_r > 40 and dist_l > 40:
                forwardtime()
            elif dist_r > 55 and dist_l > 55:
                forwardtime()

        sleep(0.05)  # Short delay between each iteration of the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main_loop()