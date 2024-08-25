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

def forward(t = 0):
    pwm.value = 1.0
    stby.on()
    ina.on()
    inb.off()
    sleep(t)
    
    
def backwards(t = 0):
    pwm.value = 1.0
    stby.on()
    ina.off()
    inb.on()
    sleep(t)
    
def stop(t = 0):  
    pwm.value = 0.0
    stby.on()
    ina.off()
    inb.off()
    sleep(t)
    
pasos = [(1, 0, 0, 0), (1, 1, 0, 0), (0, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 0), (0, 0, 1, 1), (0, 0, 0, 1)]
  
ins = [(in1), (in2), (in3), (in4)]
    
def right(ciclos):
    for _ in range(ciclos):
        for p in pasos: 
            for index, a in enumerate(p):
                if a:
                    ins[index].on()
                    
                else:
                    ins[index].off()
            sleep(0.001)
            
def left(ciclos):
    for _ in range(ciclos):
        for p in reversed(pasos): 
            for index, a in enumerate(p):
                if a:
                    ins[index].on()
                    
                else:
                    ins[index].off()
            sleep(0.001)