Welcome 🤩 ! 
We are Team Révine, proudly representing our country Perú 🇵🇪 🤖 !
====
<p align = "center">
  <img src = "https://github.com/user-attachments/assets/d41e4236-aab7-4a30-a2f4-86d483993c72">
  </p>

+ Team's Name: ***Révine***
+ Car's Name: ***Riska***
+ Teammates: ***Mafer Zambrano & Isa Gonzales***
+ Match Name: ***Robotek***

## About us!

### 1.1 Team presentation

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/e5ef3311-5d4e-47c4-966b-c02dc7470dbe",  width = "700px">
  </p>

---
### *Maria Fernanda Zambrano*
🥈 🧑‍🚀 🦢 🏛️ 🎧 🏎️ 🏁 🚀 🌙 🔭 

Age: 17

Hi! My name is Mafer and I am from Peru. Some of my hobbies are swimming, reading, and playing instruments. A fun fact about me is that I am a huge F1 fan!

---
<p align = "center">
  <img src = "https://github.com/user-attachments/assets/0ae75f01-ae9e-49fe-a418-98b065694f57",  width = "700px">
  </p>

### *Isabella Gonzales*
🐨 🤖 🥐 🌟 🥋 🎨 🎼 🥧 🍀

Age: 15

Hello! 
My name is Isa and I am from Peru. 
I love music (singing and playing the guitar), making origami, and painting. 
A fun fact about me is that I sang in the National Theather wearing pijamas when I was 6.

### 1.2 Team Management

Our project is the product of a collaborative effort by a talented and dedicated team, with each member contributing their unique expertise. As students of Robotek from Lima, Peru, we have learned valuable skills in robotics and technology. To learn more about our history and participations, follow us on [Instagram](https://www.instagram.com/ro_bo_tek?igsh=MXZydWFtamlzbHd4ag==).

+ ***Team Supervisor:*** Alejandro Garayar
+ ***Coach:*** Renzo Damian

### 1.3 Why did we choose to participate?

We see this project as more than just a competition. It is a chance to be creative, work together, and overcome challenges—both in the design and in ourselves. By designing our robot, we are not creating just a machine but a mixture of our electronic and coding skills, and innovation.

This experience has reminded us that endorsing difficulties means finding solutions where others see problems and that we can have fun and enjoy the process. So, we thank being part of this olympiad: it has pushed us beyond the limits, broadening our minds, and, most of all, we had a great time!

## About the car!

### 2.1 Which is our autonomous car's logic?

1. The program will begin with the initialization of sensors, camera, and variables. Once started, the car will enter a continuous loop with the main function running endlessly. In each loop iteration, *it will capture a frame from the camera and will read input from various sensors*, including distance and reflectance sensors.
2. The captured frame  is then analyzed to detect obstacles, and if one is found, its color is identified as either red or green. *The navigation strategy adjusts the car to pass on the right side for red obstacles and on the left side for green ones, while continuing with PID control if no obstacle is detected.* Steering adjustments are combined with the obstacle avoidance strategy and PID control to manage the car’s movement. The system also monitors proximity to obstacles, performing avoidance maneuvers if too close, reducing speed when necessary, or maintaining normal speed otherwise.
3. The car moves forward based on the calculated steering and speed. *Reflectance sensors are used to count the number of laps completed.* If all required laps are finished, the car navigates to the parking area and performs parallel parking; if not, the loop continues. Finally, the program ends after successful parking or if interrupted.

### *PID Controller*

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/9bc4ade3-cc89-4615-9778-3569b1e8419f">
  </p>

### Flow Diagram

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/7294caf2-8c36-4763-9ca8-ecd5782a64da">
  </p>

### 2.2 Why Python and C++?

Python and C++ are two widely used languages, representing the best of both worlds. While one is used for fast and flexible development, the other can be implemented for tasks that require high performance. However, together they provide a solution for a system like ours, where we need to control hardware while efficiently processing data at the same time.

1. ***Complementing the strengths of both languages:*** Python is known for being a high-level language, easy to write and read, and excellent for rapid development, proof of concepts, and handling complex tasks such as data analysis, hardware control, and machine learning. C++, on the other hand, is highly efficient in terms of speed and optimization, making it ideal for performance-critical tasks like real-time sensor handling and signal processing.
2. ***Management of libraries:*** Both languages contain a large number of easy-to-use libraries, ranging from web interface management, computer vision, and network handling to direct hardware manipulation. This allows for efficient work and rapid development of advanced functionalities without having to program them from scratch.
3. ***Use in different platforms:*** We can use Python on boards like the Raspberry Pi for general control tasks, vision, etc., where Python is commonly used because it offers extensive libraries that facilitate interaction with the operating system. In the case of C++, it will be used on Arduino. Microcontrollers like the one we will use are typically programmed in C++ because this language allows for more precise control, lower memory usage, and lower latency, which is essential when working with limited resources and tasks that require high efficiency, such as handling sensors in real time.
4. ***Performance and flexibility:*** C++ for better performance, such as sensor reading and processing; and Python for greater flexibility in handling advanced logic, such as data manipulation and integration with interfaces. This way, the versatility and communication of both libraries are fully leveraged.

## 3. Our road to success!

### *3.1 Designing the prototype*

We started by making a carton-prototype based on the turning mechanism and following the official documentation rules. This was our initial prototype:

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/06523245-8f3e-4c9d-9fc8-b9322338aac1", width = "650px">
  </p>

> [!TIP]
> In order to choose the apropiate materials, we made a design and a table of components with all our options. Then, we selected the ones that seemed the most efficient to us.

<p align="center">
  <img src="https://github.com/user-attachments/assets/8cda5ee6-cf6c-44be-bf7e-c29f5a3abca0" width="400px">
  <img src="https://github.com/user-attachments/assets/58097104-9be4-432f-a44f-7228804fc0a0" width="400px">
  </p>  

We decided to use these components:

### Bill of materials (BOM)
| Component | Quantity | Function |
| :---: | :---: | --- |
| ⁠Raspberry Pi 4 | 1 | A microcomputer that acts as the main brain of the system, capable of running operating systems and handling complex processing tasks. |
| Arduino Nano | 1 | A compact microcontroller used for control tasks and processing sensor signals. |
| Arduino Nano Expansion Shield | 1 | An expansion board for the Arduino Nano that facilitates the connection of various modules and sensors. |
| ⁠Li-Po Battery 3.7v 1000 mAh (2S) | 2 | A lithium polymer battery that provides portable, high-density power. |
| NovaMax Motor 400 Rpm | 1 | A high-speed DC motor used for propelling the cart |
| Stepper Motor 28YBJ-48 | 1 | A stepper motor used for precise movements, ideal for position control applications. |
| Driver ULN2003 | 1 | A motor driver for the stepper motor, providing the necessary current for its operation. |
| Driver TB6612 | 1 | A DC motor driver that allows efficient control of motors using control signals. | 
| Breadboard Power Supply Model Adapter Shield MB102 3.3v/5v | 1 | A regulated power supply for breadboards, providing 3.3V and 5V voltages. |
| Power Bank: 5v 3A 12000 mAh | 1 | A portable power source used to power the Raspberry Pi and other components. | 
| QTR-1A Sensors | 2 | IR reflection sensors used to detect the presence or absence of nearby objects. |
| ⁠IR Sensors Sharp GP2Y0A21 | 3 | An IR distance sensor that measures the distance of nearby objects using an infrared beam. | 
| MPU6050 Accelerometer & Gyroscope Sensor | 1 | A sensor that measures acceleration and rotation on three axes, enabling precise motion and orientation tracking. |
| ⁠Webcam | 1 | A camera used for capturing images and videos, can be used for computer vision or live streaming. |
| Capacitor 10uF | 1 | An electronic component used to store charge and smooth out voltage fluctuations. | 
| Blue Color Rubber Wheels 27mm | 2 | Allows the car to move back and forth. |
| Rubber TT Tires Wheels 12mm | 2 | Allows the car to move and turn. |
| Jumper Cables | - | Used to connect various components together. |
| USB Cable | 1 | A cable to connect the Arduino Nano to the Raspberry Pi4. |
| Switch Button | 1 | Button that signals the Raspberry Pi to start its routine. |
| Push Button | 1 | Button that powers the system. |

### Reasons for choosing our sensors

By choosing **QTR-1A** and **Sharp GP2Y0A21** sensors, you ensure precise, reliable, and cost-effective solutions for our robot.

+ QTR-1A Sensors:

  + ***Fast response and high precision for line detection:*** We need a high-speed robot that operates in fast-moving applications. Having the need of real-time feedback for quick adjustments and control, we chose the sensor for its rapid signal process and using the infrared LED and phototransistor pair we detect the surface lines and light.
  + ***Compact and low power consumption:*** The small footprint allows easy integration into compact designs without adding extra weight and, also, help us optimize energy efficiency in battery-operated systems like ours, allowing us to conserve battery life for the competition.
 
+ Sharp GP2Y0A21 IR Sensors:

  + ***Accurate distance measurement:*** It can be integrated with microcontrollers and other analog signal processing systems to provide precise distance readings in the obstacle detection task by using the infrared triangulation technology to measure distances from 10 cm to 80 cm 
  + ***Reliable and durable:*** The sensor is known for its long-lasting performance and efficiently operation in a wide range of conditions, not only during variations in temperature or humidity, but when there is light interference from the surrounding environment, too, wichi we think could possibly happen during the competition.

+ MPU6050 Accelerometer & Gyroscope Sensor:
  
  + ***Motion tracking:*** With both an accelerometer and gyroscope, we can precisely track the robot’s movement and angular velocity to determine our robot's speed, direction, and turns. Moreover, it provides real-time feedback on the robot's orientation (pitch, roll, and yaw), allowing it to maintain balance and stability.
  + ***Inertial navigation:*** * The sensor will allow us to perform dead reckoning, estimating our robot’s position based on movement data even in environments without GPS. Also, we will detect impacts and take evasive actions, making the robot smarter in navigating through dynamic environments.

### Wiring diagram

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/0290cbf9-f94b-4d9c-834c-3aba63771e25", width = "850x">
  </p>

---
### *3.2 Code for the camera*

We started by making the `detectColors` and `util.py` code for the camera. On it, we made the camera descompose the image into pixels, which detected the color it sees in RGB format and then converted it into a new HSV format. We used the color palette based on hue (HUE) to select the color and set the limits with which the range of colors we are looking for will be detected. Once the color code in HSV is obtained, we compared it with a specific range of values. If the desired color is within our palette, it will be highlighted with an internal frame.

#### ***Step by Step***

+ ***Visual Studio Code:*** We opened Visual Studio Code, downloaded *Python* and imported these libraries.
```
import cv2
import numpy as np
from PIL import Image
from util import get_limits
```
+ ***`get_limits` function:*** The camera took a color in `BGR` format and converted it to `HSV` to extract the hue component. It then defined a range of `±10` around the hue value and returned lower and upper bounds for filtering the color in the `HSV` color space. This enabled more effective color detection by accounting for variations in the color's hue.
+ ***Webcam initialization and color setup:*** The program initialized the webcam using `cv2.VideoCapture(1)` to capture live video. It defined two colors, `red` and `blue`, in `BGR` format, which was used for detecting those specific colors within the video feed.
+ ***Main Loop with frame capture:*** The program will continuously capture frames from the webcam. Each frame was converted from `BGR` to `HSV` format, which allowed more effective color-based filtering. The frame was then processed to isolate the areas that match the target color using the previously calculated `HSV` limits. If a match is found, a rectangle is drawn around the detected color in the frame, which is then displayed in a window as shown:

<p align = "center">
  <img width="900" alt="colorDetection" src="https://github.com/user-attachments/assets/fcd87a76-d15e-44bb-84c2-3114a56d85bc">
</p>

---
### *3.3 Printing the prototype and ensambling*

We proceeded to print our first prototype using 3D printing. Once we had all the parts ready, we began the assembly process: we added the motors and the wheels, selected to ensure proper traction and optimal movement.  

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/dca1240a-ef3a-4b02-b663-73f74957ab60", width = "650px">
  </p>

---
### *3.4 Code for the Raspberry PI 4*

We used the MicroSD card to connect to one of the computers, which we then linked to the Wi-Fi network. We configured its MicroSD card and began developing the code. This includes the modules for `motor.py`, `detectColors.py`, `ser.py`, and `main.py`.

#### Step by Step

+ #### Step 1: `ser.py`
  
  + ***Visual Studio Code:*** We opened Visual Studio Code and imported this library.
  ```
  import serial
  ```
  + ***Serial communication setup:*** We started the connection using the `serial.Serial()` function, with `/dev/ttyUSB0` as our serial port, a baud rate of `9600`, and a timeout of 1 second.
  + ***Buffer management:*** Then, we set up the function `read_sensors()` to manage the incoming data from the serial port. A `buffer string` was used to accumulate the incoming data. The `ser.read(ser.inWaiting())` method read all available bytes from the serial buffer checking for the presence of a newline character `\n` to determine the end of a complete message.
  + ***Data parsing:*** When a newline is detected in the buffer, the accumulated data was split into separate lines using `split('\n')`. The second-to-last line (`last_received`) was processed and stripped of any trailing whitespace and split by commas. The function ensures that exactly five values are received by checking the length of the split data, which are then converted to integers and assigned to corresponding sensor variables (`dist_l`, `dist_t`, `dist_r`, `qtr_L`, `qtr_R`).

+ #### Step 2: `main.py `

---
### *3.5 Code for the motors*

In `motor.py`, we implemented the forward and backward motor functions: FORWARDS and BACKWARDS. We developed the turning logic using the Stepper motor control (LEFT and RIGHT) and created a sequence using a 'for' loop to manage the Stepper motor movement.

> [!NOTE]
> In the end, we decided to change the motor model to improve its efficiency. However, the code remains the same.

#### Step by Step

+ ***Visual Studio Code:*** We opened Visual Studio Code and imported these libraries.
```
from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep
```
+ ***Initialization of devices:*** We initialized the GPIO pins that controled both the motor's Pulse Width Modulation (PWM) and digital outputs for controlling motor direction and standby mode. It set up digital outputs for pins `IN1`, `IN2`, `IN3`, and `IN4`, and configured a PWM signal for motor speed control through `pin 12`. The pins `INA` and `INB` were used to control motor direction, and pin STBY was used for enabling and disabling the motor.
+ ***Motor control functions:*** We defined three functions to control the motor: `forward()`, `backwards()`, and `stop()`. The `forward()` function turns the motor on by setting the PWM to full power, enabling standby mode, and setting `INA` high while `INB` is low to move forward. Similarly, `backwards()` sets `INA` low and `INB` high to reverse the motor direction. And, the `stop()` function turns off both `INA` and `INB` and sets the PWM to zero, effectively stopping the motor.
+ ***Stepper Motor and configuration:*** By using the list called `pasos`, we set up step sequences for the stepper motor, which contains tuples representing the on/off states of four pins (IN1 to IN4) that control the motor’s phases.
+ ***Rotation functions: `left()` and `right()`:*** Both functions were defined to rotate the stepper motor either to the right or left. The `right()` function iterates through the steps in `pasos` to activate the motor coils in sequence, turning the motor clockwise for a specified number of cycles. The `left()` function works similarly but uses the reversed `pasos` list to rotate the motor counterclockwise.
  
---
### *3.6 Code for the Arduino*

We used an Arduino Nano and developed the `analogsensor.ino` code, which, along with Sharp sensors, allowed us to measure distance from three different angles: front, left, and right. We collected the data and printed it to the serial port for monitoring. Subsequently, we connected the Arduino to the Raspberry Pi and, through the code in `ser.py`, read and processed the data provided by the sensors.

#### ***Step by Step***

+ ***Arduino IDLE:*** We opened the Arduino IDLE platform and imported these libraries.
```
#include "SharpIR.h"
#include "QTRSensors.h"
```
+ ***Pin and variable definitions:*** We defined the IR sensor model as `1080` and used three analog pins (`IRP1`, `IRP2`, `IRP3`) to connect three Sharp IR sensors. Then, we initialized a `QTRSensors QTRA` object to manage the reflectance sensors and read them with `sensor_values[2]`, connected to pins A3 and A4. In the case of pins A0, A1, and A2, we created three objects: `SharpIR sensor1`, `sensor2`, and `sensor3`, respectively.
+ ***`setup()` function:*** The QTR sensors were configured to operate in analog mode using `qtra.setTypeAnalog()` and the pins A3 and A4 were specified as inputs for the reflectance sensors via qtra.setSensorPins().
+ ***`loop()` function:*** It then read the analog values from the three Sharp IR sensors using `analogRead()` and calculated the distance to nearby objects using the `distance()` function for each sensor. Finally, the distances from the three Sharp sensors, along with the reflectance sensor values, were printed to the serial monitor using `Serial.print()`, separated by commas with a 300 ms delay (`delay(300)`) per information.
---
### *3.7 Designing and printing the second prototype*

We redesigned the prototype after realizing that we needed to adapt the new components to the cart. We 3D printed only the essential parts, such as the steering system and motor mounts, while the rest was cut from acrylic to keep the structure light and sturdy.

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/7b2bdaf5-1f30-4a61-9fc3-0eed9f7d6961", width = "650px">
  </p>
  
---
### *3.8 Designing and printing the last prototype*

We printed the prototype for the third and final time, adding an additional level to better distribute the components and provide a mount for the webcam. We also slightly modified the design of the motor mount to fit the PowerBank, ensuring a perfect fit and a more efficient arrangement of all elements.

> [!NOTE]
> To optimize performance and extend the cart's runtime, we decided to replace the traditional batteries with LiPo cells.

---
### *3.9 Code for the turns*

---
### *3.10 Code for avoiding obstacles*

> [!NOTE]
> About the `main.py`...

---
### *3.11 Code for parking*
