from motor import forward, backwards, stop, left, right
from ser import read_sensors
from time import sleep, time
import cv2
import numpy as np

# Constants
ROBOT_LENGTH = 30  
PARKING_SPACE_LENGTH = 1.25 * ROBOT_LENGTH
PARKING_WIDTH = 20  

FORWARD_SPEED = 1.0
BACKWARD_SPEED = 1.0
TURN_TIME = 0.6
PARKING_DISTANCE_TOLERANCE = 5  

def measure_parking_space():
    """
    Measures the side distance to identify if there is a large enough parking space.
    """
    while True:
        sensor_values = read_sensors()
        dist_l, dist_t, dist_r, qtr_L, qtr_R = sensor_values
        
        if dist_r > PARKING_SPACE_LENGTH:  #detects if space is large enough
            print(f"Espacio de estacionamiento detectado: {dist_r} cm")
            return True  # it detetected an available site
        forward(FORWARD_SPEED, 0.3)  # continues moving and measuring
        sleep(0.1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return False

def parallel_parking():
    """
    Executes the parallel parking maneuver.
    """
    print("Executing the parallel parking maneuver.")
    
    # 1. forward until align
    forward(FORWARD_SPEED, 0.5)
    stop(0.05)

    # 2. turns to left while goes backward
    right(300)  
    backwards(BACKWARD_SPEED, TURN_TIME)
    stop(0.05)

    # 3. returns the wheels
    left(300)  # turns to left
    backwards(BACKWARD_SPEED, TURN_TIME)
    stop(0.05)
    
    print("Parking complete.")
    
def main_loop():
    """
    Main loop where it searches for a parking space and executes the maneuver.
    """
    while True:
        # searchs for the parking space
        if measure_parking_space():
            # once detected the sectors, parks
            parallel_parking()
            break  # breaks the loop after do it
        sleep(0.1)

if __name__ == "__main__":
    main_loop()