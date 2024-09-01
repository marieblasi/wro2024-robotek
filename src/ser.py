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
        if len(values) == 5:
            dist_l, dist_t, dist_r, qtr_L, qtr_R = map(int, values)
            print(f"Sensor 1: {dist_l}, Sensor 2: {dist_t}, Sensor 3: {dist_r}, Sensor 4: {qtr_L}, Sensor 5: {qtr_R}")
            return dist_l, dist_t, dist_r, qtr_L, qtr_R
        else:
            print("Received incomplete data")
            return None
    return None