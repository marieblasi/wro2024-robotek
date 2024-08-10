from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep

PWM = 12
INA = 16
INB = 18
STBY = 22

IN1 = 5
IN2 = 6
IN3 = 23
IN4 = 24

in1 = DigitalOutputDevice(IN1)
in2 = DigitalOutputDevice(IN2)
in3 = DigitalOutputDevice(IN3)
in4 = DigitalOutputDevice(IN4)

pwm = PWMOutputDevice(PWM)
ina = DigitalOutputDevice(INA)
inb = DigitalOutputDevice(INB)
stby = DigitalOutputDevice(STBY)

i = 1

while True:

    pwm.value = 1.0
    stby.on()
    ina.on()
    inb.off()


    i += 1


    if i < 200:

        #Derecha

        print(i)

        in1.on()
        in2.off()
        in3.off()
        in4.off()

        sleep(0.001)
        
        in1.on()
        in2.on()
        in3.off()
        in4.off()

        sleep(0.001)

        in1.off()
        in2.on()
        in3.off()
        in4.off()

        sleep(0.001)
        
        in1.off()
        in2.on()
        in3.on()
        in4.off()

        sleep(0.001)

        in1.off()
        in2.off()
        in3.on()
        in4.off()

        sleep(0.001)
        
        in1.off()
        in2.off()
        in3.on()
        in4.on()

        sleep(0.001)

        in1.off()
        in2.off()
        in3.off()
        in4.on()

        sleep(0.001)
        
        in1.on()
        in2.off()
        in3.off()
        in4.on()

        sleep(0.001)




    #Izquierda

    in1.on()
    in2.off()
    in3.off()
    in4.on()

    sleep(0.001)

    in1.off()
    in2.off()
    in3.off()
    in4.on()

    sleep(0.001)

    in1.off()
    in2.off()
    in3.on()
    in4.on()

    sleep(0.001)

    in1.off()
    in2.off()
    in3.on()
    in4.off()

    sleep(0.001)

    in1.off()
    in2.on()
    in3.on()
    in4.off()

    sleep(0.001)

    in1.off()
    in2.on()
    in3.off()
    in4.off()

    sleep(0.001)

    in1.on()
    in2.on()
    in3.off()
    in4.off()

    sleep(0.001)
        
    in1.on()
    in2.off()
    in3.off()
    in4.off()

    sleep(0.001)

