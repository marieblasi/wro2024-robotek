import serial

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout = 1)

while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            values = line.split(',')
            if len(values) == 3:
                sensor1, sensor2, sensor3 = map(int, values)
                print(f"Sensor 1: {sensor1}, Sensor 2: {sensor2}, Sensor 3: {sensor3}")
            else:
                print("Received incomplete data")