# imported libraries and other arhives
from motor import forward, backwards, stop, left, right
from ser import read_sensors
from time import sleep, time
from detectColors import analyze_sides
import cv2
from gpiozero import Button

# initialize with the start button
button = Button(21)

# wait for button press to start
print("Press the button to start...")
button.wait_for_press()
print("Button pressed. Starting the program...")

# called our camera
cap = cv2.VideoCapture(0)

kp = 2.9     # should be greater than  kd
kd = 0.8
ki = 0.0001  # should be a minimun value value


FORWARD_SPEED = 1
FORWARD_TIME = 0.25
BACKWARD_SPEED = 0.7
BACKWARD_TIME = 0.7
STOP_TIME = 0.01

# declared variables
previous_error = 0 
last_time = time()
integral = 0
moving_time = 0


## DEFINITIONS

#PID controller
def pid_control(d_left, d_right):
    global previous_error, last_time, integral, moving_time
    dt = moving_time
    moving_time = 0
    e = d_right - d_left   # error
    P = kp * e
    integral = integral + (e * dt)
    derivative = (e - previous_error) / dt if dt > 0 else 0
    I = ki * integral
    D = kd * derivative
    print(f'P: {P}; I: {I}; D: {D}')   # PID

    previous_error = e
    return max(min(int(P + I + D), 300), -300)

# steer logic
def steer_logic(steering_change):
    global moving_time
    abs_steering = abs(steering_change)
    
    if steering_change < 0:
        print(f'Turning left: {steering_change}')
        left(abs_steering)
    else:
        print(f'Turning right: {steering_change}')
        right(abs_steering)
        
    start_time = time()
    forward(FORWARD_SPEED, FORWARD_TIME)
    moving_time = time() - start_time
    print("Forward PID")
    
    stop()

    if steering_change < 0:
        print(f'Turning right: {steering_change}')
        right(abs_steering)
    else:
        print(f'Turning left: {steering_change}')
        left(abs_steering)
    stop()


## MAIN LOOP

while True:    
    # read camera and sensors
    ret, frame = cap.read()
    sensor_values = read_sensors()
    
    # specify sensors and the camera angles
    if sensor_values:
        # cv2.imshow("frame", frame)
        dist_l, dist_t, dist_r, qtr_L, qtr_R = sensor_values
        steering_change = pid_control(dist_l, dist_r)
        cam_direction = analyze_sides(frame)
        print(f"Cam Direction: {cam_direction}")

        # first case (if near the walls)
        if dist_t < 18 or dist_l < 10 or dist_r < 10:
            stop(STOP_TIME)
            print("-----backwards------")
            e = abs(dist_l - dist_r)  # defining the error value

            # if there is space left...
            if e > 50:
                # you follow the SENSORS
                # if left distance is greater that right's...
                if dist_l > dist_r:
                    right(abs(250))
                    print("Back")
                    backwards(t=BACKWARD_TIME, _pwm=BACKWARD_SPEED)
                    stop(t=STOP_TIME)
                    left(abs(250))
                # if right distance is greater that left's...
                elif dist_r > dist_l:
                    left(abs(250))
                    print("Back")
                    backwards(t=BACKWARD_TIME, _pwm=BACKWARD_SPEED)
                    stop(t=STOP_TIME)
                    right(abs(250))
            else:
                # you follow the CAMERA
                # if you see more space at the front-right side...
                if cam_direction == "right":
                    left(abs(250))
                    backwards(t=BACKWARD_TIME, _pwm=BACKWARD_SPEED)
                    stop(t=STOP_TIME)
                    right(abs(250))
                # if you see more space at the front-left side...
                elif cam_direction == "left":
                    right(abs(250))
                    backwards(t=BACKWARD_TIME, _pwm=BACKWARD_SPEED)
                    stop(t=STOP_TIME)
                    left(abs(250))
                # if you see the same amount of space at both sides...
                else:
                    backwards(t=BACKWARD_TIME, _pwm=BACKWARD_SPEED)
                    stop(t=STOP_TIME)
        
        # second case (if there are no walls)
        elif dist_t > 55 and dist_r > 40 and dist_l >40:
            forward(t=FORWARD_TIME, _pwm=FORWARD_SPEED)
        
        # third case (when space at both sides)
        elif dist_r > 55 and dist_l > 55:
            # you follow the CAMERA
            # when going to the left...
            if cam_direction == "left":
                    left(abs(250))
                    forward(t=FORWARD_TIME, _pwm=FORWARD_SPEED)
                    stop(t=STOP_TIME)
                    right(abs(250))
            # when going to the right...
            elif cam_direction == "right":
                    right(abs(250))
                    forward(t=FORWARD_TIME, _pwm=FORWARD_SPEED)
                    stop(t=STOP_TIME)
                    left(abs(250))
            # when going forward...
            else:
                    forward(t=FORWARD_TIME, _pwm=FORWARD_SPEED)
                    stop(t=STOP_TIME)
                
            print(analyze_sides(frame))

        # last case (follow the steer logic)
        else:
           steer_logic(steering_change)  
    
    # delay
    sleep(0.05)
