from motor import forward, backwards, stop, left, right
from ser import read_sensors
from time import sleep

steering_angle = 0 
# -200 to 200
while True:
    sensor_values = read_sensors()
    
    if sensor_values:
        sensor1, sensor2, sensor3 = sensor_values
        print(sensor1, sensor3)
        dx = sensor3 - sensor1
        if ( abs(dx) > 10):
            if (dx > 0):
                left(20)
                # steering_angle = steering_angle + (-100)
            if (dx < 0):
                right(10)
        
        # if sensor2 > 18:
        #     forward()
        # else:
        #     stop()
        sleep(0.1)
    

