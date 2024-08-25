import serial

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout = 1)

buffer_string = ''

def read_sensors():
    global buffer_string
    global last_received
    buffer_string = buffer_string + ser.read(ser.inWaiting()).decode('utf-8', errors = "ignore")
    if '\n' in buffer_string:
        lines = buffer_string.split('\n')
        last_received = lines[-2]
        buffer_string = lines[-1]
        line = last_received.rstrip()
        values = line.split(',')
        if len(values) == 3:
            sensor1, sensor2, sensor3 = map(int, values)
            #print(f"Sensor 1: {sensor1}, Sensor 2: {sensor2}, Sensor 3: {sensor3}")
            return sensor1, sensor2, sensor3
        else:
            print("Received incomplete data")
            return None
    return None