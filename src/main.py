from motor import forward, backwards, stop
from ser import read_sensors

while True:
    sensor_values = read_sensors()
    
    if sensor_values:
        sensor1, sensor2, sensor3 = sensor_values
        print(sensor1, sensor2, sensor3)
        
        if sensor2 > 18:
            forward()
        else:
            stop()
        

    

