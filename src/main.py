from motor import forward, backwards, stop, left, right
from ser import read_sensors
from time import sleep, time

kp = 0.8
kd = 0.01
ki = 0.01

previous_error = 0 
last_time = time()
integral = 0

def pid_control(d_left, d_right):
    global previous_error, last_time, integral
    current_time = time()
    e = d_left - d_right
    P = kp * e
    dt = current_time - last_time
    integral = integral + (e * dt)
    derivative = (e - previous_error) / dt
    I = ki * integral
    D = kd * derivative
    print(f'P: {P}; I: {I}; D: {D}')

    previous_error = e
    last_time = current_time
    return int(P + I + D) 

steering_angle = 0 
while True:
    sensor_values = read_sensors()
    
    if sensor_values:
        sensor1, sensor2, sensor3 = sensor_values
        print(sensor1, sensor3)
        steering_change = pid_control(sensor1, sensor3)
        print(f'steering change : {steering_change}')
        if (steering_change < 0):
            left(abs(20))
        elif (steering_change > 0):
            right(abs(20))