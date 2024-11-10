Welcome 🤩 ! 
We are Team Révine, proudly representing our country Perú 🇵🇪 🤖 !
====
<p align = "center">
  <img src = "https://github.com/user-attachments/assets/196f69c0-0233-43e6-970e-4f6ab1ee7f02">
  </p>

## **Table of Contents**

+ Team's Name: ***Révine***
+ Car's Name: ***Riska***
+ Teammates: ***Mafer Zambrano & Isa Gonzales***
+ Match Name: ***Robotek***

- [1. 🤖 About us!](#39-about-us!)
  - [1.1 🌟 Team presentation](#41-team-presentation)
  - [1.2 🚀 Our Goal](#12-our-goal)
- [2.0 🛠️ Hardware](#2-hardware)
  - [2.1 🔧 Components](#21-components)
    - [2.1.1 ⚡ Power Source](#211-power-source)
    - [2.1.2 🧱 Construction Materials](#212-construction-materials)
    - [2.1.3 🔌 Connectors and Cables](#213-connectors-and-cables)
    - [2.1.4 🛠️ Tools and Adhesives](#214-tools-and-adhesives)
    - [2.1.5 💡 Other Electronic Components](#215-other-electronic-components)
- [3.0 Models](#3-models)
  - [3.1 PCB Board](#31-pcb-board)
  - [3.2 Ackerman Steering System](#32-ackerman-steering-system)
  - [3.3 Differential System](#33-differential-system)
    - [3.3.1 Motors](#331-motors)
- [4.0 TOF System](#4-tof-system)
  - [4.1 First Phase](#41-first-phase)
  - [4.2 Second Phase](#42-second-phase)
  - [4.3 Third Phase](#43-third-phase)
- [5.0 Sensores](#50-sensores)
  - [5.1 TSC3200 color sensor](#51-tsc3200-color-sensor)
  - [5.2 ESP32 CAM](#52-esp32-cam)
    - [5.2.1 CODE ESP32 CAM](#521-code-esp32-cam)

## 1. About us!

### 1.1 Team presentation

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/664a8f36-87c0-433d-9845-4cd4cd0c1975">
  </p>

---

|  | 🐨 🤖 🥐 🌟 🥋 🎨 🎼 🥧 🍀 | 🥇 🧑‍🚀 🦢 🏛️ 🎧 🏎️ 🏁 🚀 🌙 🔭 |
| :---: | :---: | :---: |
| **Name** | Isabella Gonzales | Maria Fernanda Zambrano |
| **Age** | 15 | 17 |
| **Role** |  |  |
| **Extra** | I love music (singing and playing the guitar), making origami, and painting. A fun fact about me is that I sang in the National Theather wearing pijamas when I was 6. | Some of my hobbies are swimming, reading, and playing instruments. A fun fact about me is that I am a huge F1 fan! |

### 1.2 Team Management

Our project is the product of a collaborative effort by a talented and dedicated team, with each member contributing their unique expertise. As students of Robotek from Lima, Peru, we have learned valuable skills in robotics and technology. 

+ ***Team Supervisor:*** Alejandro Garayar
+ ***Coach:*** Renzo Damian

### 1.3 Why did we choose to participate?

We see this project as more than just a competition. It is a chance to be creative, work together, and overcome challenges—both in the design and in ourselves. By designing our robot, we are not creating just a machine but a mixture of our electronic and coding skills, and innovation.

This experience has reminded us that endorsing difficulties means finding solutions where others see problems and that we can have fun and enjoy the process. So, we thank being part of this olympiad: it has pushed us beyond the limits, broadening our minds, and, most of all, we had a great time!

## About the car!

### 2.1 Which is our autonomous car's logic?

1. The program will begin with the initialization of sensors, camera, and variables. Once started, the car will enter a continuous loop with the main function running endlessly. In each loop iteration, *it will capture a frame from the camera and will read input from various sensors*, including distance and reflectance sensors.
2. The captured frame  is then analyzed to detect obstacles, and if one is found, its color is identified as either red or green. *The navigation strategy adjusts the car to pass on the right side for red obstacles and on the left side for green ones.* Steering adjustments are combined with the obstacle avoidance strategy to manage the car’s movement. The system also monitors proximity to obstacles, performing avoidance maneuvers if too close, reducing speed when necessary, or maintaining normal speed otherwise.
3. The car moves forward based on the calculated steering and speed. *Reflectance sensors are used to count the number of laps completed.* If all required laps are finished, the car navigates to the parking area and performs parallel parking; if not, the loop continues. Finally, the program ends after successful parking or if interrupted.

### Flow Diagram

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/7294caf2-8c36-4763-9ca8-ecd5782a64da">
  </p>

### 2.2 Why Python?

Python is a widely used language, representing the best. It is used for fast and flexible development and, also, implemented for tasks that require high performance providing a solution for a system like ours, where we need to control hardware while efficiently processing data at the same time.

1. ***Complementing the strengths of both languages:*** Python is known for being a high-level language, easy to write and read, and excellent for rapid development, proof of concepts, and handling complex tasks such as data analysis, hardware control, and machine learning.
2. ***Management of libraries:*** This language contains a large number of easy-to-use libraries, ranging from web interface management, computer vision, and network handling to direct hardware manipulation. This allows for efficient work and rapid development of advanced functionalities without having to program them from scratch.
3. ***Use in different platforms:*** We can use Python on boards like the Raspberry Pi for general control tasks, vision, etc., where Python is commonly used because it offers extensive libraries that facilitate interaction with the operating system. 
4. ***Performance and flexibility:*** Python can be used for greater flexibility in handling advanced logic, such as data manipulation and integration with interfaces.

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
Component | Quantity | Function |
 :---: | :---: | --- |
| Raspberry Pi 4 | 1 | A microcomputer that acts as the main brain and the **Host Controller** of the system, capable of running operating systems and handling complex processing tasks. |
| RRC Lite Controller | 1 | Integrates several elements: ***ROS expansion board, High-Frequency PID Control, Motor Closed-Loop Control, Servo Control and Feedback, IMU Data Acquisition, Power Status Monitoring***, and a ***Power Switch***. |
| STL-19P TOF Lidar | 1 | Provides precise, 360-degree distance measurements for real-time navigation and obstacle detection in dynamic environments. |
| 15 kg.cm Digital Servo | 1 | A servo to control the Ackerman system to make precise movements. |
| 65 mm Anti-Slip Rubber Wheel | 1 | Allows the car to move back, forth, and make turns. |
| 310 DC geared Encoder Motor | 1 | A high-speed DC motor used for propelling the car. |
| Monocular Camera | 1 | A camera used for capturing images and videos, can be used for computer vision or live streaming. |
| Jumper Cables | 6 | Component | Used to connect various components together. |
| USB Cable | 3 | A cable to connect the Raspberry Pi4 to the camera, Raspberry to Lidar, and Raspberry to Controller. |
| ⁠Li-Po Battery 7.4 V 2200 mAh 20C | 1 | A lithium polymer battery that provides portable, high-density power. |

### Reasons for choosing our sensors and camera

+ STL-19P TOF Lidar:

  + ***Precise environmental mapping***: With its ±10mm accuracy, the STL-19P enables precise positioning, essential for navigating narrow or intricate sections of the obstacle course. This allows our robot to make calculated movements without collisions or deviations.
  + ***Real-time obstacle avoidance***: With its fast sampling rate, the LiDAR can detect and react to obstacles dynamically, ensuring smoother movement through the course.
  + ***Enhanced performance in varied lighting***: Its high tolerance for ambient light up to 60,000 lux and ability to detect glass is essential, where lighting conditions vary. This feature ensures our robot maintains consistent performance, accurately detecting objects and avoiding potential pitfalls like transparent or shiny obstacles.

+ Monocular Camera:

  + ***Color detection***: Since graphical color detection is a core part of your project, the camera can precisely identify various colors on the course. This enables our robot to execute programmed actions based on specific color cues, which is crucial for the Obstacle challenge, which requires interaction with color-based objects.
  + ***Spatial awareness through data fusion***: When combining camera data with our sensor, the robot gains a richer understanding of its environment. The camera provides detailed visual context that complements other data sources, leading to a more informed and adaptable navigation strategy.

### Wiring diagram

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/1a49de83-32af-4f52-9886-47c35641fcf5", width = "850x">
  </p>

---
## First Version!
### *4.1 Code for the camera*

We started by making the code for the camera. On it, we made the camera descompose the image into pixels, which detected the color it sees in RGB format and then converted it into a new HSV format. We used the color palette based on hue (HUE) to select the color and set the limits with which the range of colors we are looking for will be detected. Once the color code in HSV is obtained, we compared it with a specific range of values. If the desired color is within our palette, it will be highlighted with an internal frame.

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

### *4.2 Printing the prototype and ensambling*

We proceeded to print our first prototype using 3D printing. Once we had all the parts ready, we began the assembly process: we added the motors and the wheels, selected to ensure proper traction and optimal movement.  

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/dca1240a-ef3a-4b02-b663-73f74957ab60", width = "650px">
  </p>

### *4.3 Code for the Raspberry PI 4*

We used the MicroSD card to connect to one of the computers, which we then linked to the Wi-Fi network. We configured its MicroSD card and began developing the code.

#### Step by Step
  
  + ***Visual Studio Code:*** We opened Visual Studio Code and imported this library.
  ```
  import serial
  ```
  + ***Serial communication setup:*** We started the connection using the `serial.Serial()` function, with `/dev/ttyUSB0` as our serial port, a baud rate of `9600`, and a timeout of 1 second.
  + ***Buffer management:*** Then, we set up the function `read_sensors()` to manage the incoming data from the serial port. A `buffer string` was used to accumulate the incoming data. The `ser.read(ser.inWaiting())` method read all available bytes from the serial buffer checking for the presence of a newline character `\n` to determine the end of a complete message.
  + ***Data parsing:*** When a newline is detected in the buffer, the accumulated data was split into separate lines using `split('\n')`. The second-to-last line (`last_received`) was processed and stripped of any trailing whitespace and split by commas. The function ensures that exactly five values are received by checking the length of the split data, which are then converted to integers and assigned to corresponding sensor variables (`dist_l`, `dist_t`, `dist_r`, `qtr_L`, `qtr_R`).

### *4.4 Code for the motors*

We implemented the forward and backward motor functions: FORWARDS and BACKWARDS. We developed the turning logic using the Stepper motor control (LEFT and RIGHT) and created a sequence using a 'for' loop to manage the Stepper motor movement.

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
  
### *4.5 Code for the Arduino*

We used an Arduino Nano and developed the code, which, along with Sharp sensors, allowed us to measure distance from three different angles: front, left, and right. We collected the data and printed it to the serial port for monitoring. Subsequently, we connected the Arduino to the Raspberry Pi and, through a different document, read and processed the data provided by the sensors.

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
## Second Version!
### *5.1 Designing and printing the second prototype*

We redesigned the prototype after realizing that we needed to adapt the new components to the cart. We 3D printed only the essential parts, such as the steering system and motor mounts, while the rest was cut from acrylic to keep the structure light and sturdy.

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/7b2bdaf5-1f30-4a61-9fc3-0eed9f7d6961", width = "650px">
  </p>
  
---
## *Last Version!*
### *6.1 Strategy*

#### *PID Controller*

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/9bc4ade3-cc89-4615-9778-3569b1e8419f">
  </p>

A PID controller adjusts system behavior by comparing a desired target value (setpoint) with the current value (measured variable) and applying corrections based on three components:

- Proportional (P): Corrects errors directly related to the current error, giving immediate response.
- Integral (I): Addresses accumulated past errors, eliminating any steady-state offset.
- Derivative (D): Reacts to the rate of change of error, smoothing the system response to prevent overshoot.

The combination of these three terms allows the PID controller to correct the system’s course precisely, leading it to the desired state without oscillation, instability, or excessive delay.

#### *Why PID Controllers?*
- Offer precise control over processes, especially in systems that require stable and accurate responses, like temperature control in HVAC systems, speed control in motors, or flow control in pipelines.
- Are effective across various industries, from manufacturing to automotive and chemical processing, because they adapt well to different types of processes and can be tuned to specific needs.
- By balancing the proportional, integral, and derivative terms, they minimize overshoot (exceeding the target) and eliminate steady-state error (any persistent difference from the target), leading to more accurate outcomes.
- Can adjust system responses to be faster or slower, depending on the application, achieving a balance between speed and stability. This is essential for processes where rapid response and minimal oscillation are needed.
- Is simpler to implement although more advanced controllers exist, requiring just three parameters to tune. Many tuning methods exist, making it straightforward to customize for different systems.

### *6.2 Designing and printing the last prototype*

We printed the prototype for the third time:
#### What we changed:
- Added an additional level to better distribute the components and provide a mount for the *webcam*.
- Slightly modified the design of the motor mount to fit the *PowerBank 12000mAh*, ensuring a perfect fit and a more efficient arrangement of all elements.
- Added 2 *QRT 1A Sensors* to improve the precision of environmental sensing while a *MPU6050 Accelerometer & Gyroscope Sensor* was included to enhance stability and orientation control.
- Changed the engine and adjusted the *Gear ratio* to provide better torque for handling challenging terrain.
- After, upgrading our batteries to *LiPo cells* to increase power capacity and efficiency, a *camera* was mounted for real-time visual feedback, and a *push button*, for easy interaction.
- Change the metal wheels to plastic ones for their lightweight properties, and the front wheels’ support was reinforced with ball bearings to reduce friction and ensure smoother movement.

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/d4e2e5f6-b742-464e-b3f9-be03cae16b6d", width = "650px">
  </p>

### *6.3 Main code* 

It was our code for the open challenge. As we tried to solve the problem of the corners and the fast detection of the walls within the three (3) minutes given, we decided to create a user-friendly code that could use the walls to find a midpoint to follow. We imported libraries such as `cv2` for camera input, `gpiozero` to control the robot with a button, and sensor/motor functions from our other documents. After initializing the robot’s camera and setting up the `PID control` constants, the program will wait for the user to press a button to start. Then, our code is descomposed into four (4) possible steps, according  to the situation, within a loop:
```
while True:    
    # it reads the camera and sensors 
    ret, frame = cap.read()
    sensor_values = read_sensors() 
    
    # specify sensors and the camera angles
    if sensor_values:
        # distance sensors
        dist_l, dist_t, dist_r, qtr_L, qtr_R = sensor_values
        steering_change = pid_control(dist_l, dist_r)
        # camera direction
        cam_direction = analyze_sides(frame)
        print(f"Cam Direction: {cam_direction}")

        # FIRST CASE (if near the walls)
        if dist_t < 18 or dist_l < 10 or dist_r < 10:
            ...
            e = abs(dist_l - dist_r)  # defining the error value

            # if there is space left...
            if e > 50:
                # you follow the SENSORS
                # if left distance is greater that right's...
                if dist_l > dist_r:
                    ...
                # if right distance is greater that left's...
                elif dist_r > dist_l:
                    ...
            else:
                # you follow the CAMERA
                # if you see more space at the front-right side...
                if cam_direction == "right":  
                    ...
                # if you see more space at the front-left side...
                elif cam_direction == "left":
                    ...
                # if you see the same amount of space at both sides...
                else:
                    ...
        
        # SECOND CASE (if there are no walls near)
        elif dist_t > 55 and dist_r > 40 and dist_l >40:
            ...
        
        # THIRD CASE (when space at both sides)
        elif dist_r > 55 and dist_l > 55:
            # you follow the CAMERA
            # when going to the left...
            if cam_direction == "left":
                    ...
            # when going to the right...
            elif cam_direction == "right":
                    ...
            # when going forward...
            else:
                    ...

        # FOURTH CASE (follow the steer logic)
        else:
           steer_logic(steering_change)  
    
    # delay
    sleep(0.05)
    
    # SHOW THE CAMERA (if desired)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

### *6.4 Code for avoiding obstacles*

We defined our robot's code for the open challenge, where we need to navigate and avoid obstacles by detecting red and green blocks using a camera, while also using distance sensors to ensure safe forward movement.

#### Step by Step

+ ***Visual Studio Code:*** We opened Visual Studio Code and imported these libraries.
```
from motor import forward, backwards, stop, left, right
from ser import read_sensors
from time import sleep, time
import cv2
import numpy as np
``` 
+ ***Caption of video frames for detection:*** The robot will continously capture video frames, convert them to the HSV color space, and apply the color masks to detect red and green blocks.
+ ***Movements:*** If a red block is detected, the robot performs a right turn, moves forward, and then turns left to maneuver around the block; for a green block, it performs a left turn first, followed by a right turn, and moves forward to bypass the obstacle. If no color block is detected, the robot uses sensor readings from the left, front, and right sides to determine if it's safe to move forward, ensuring that no obstacles are too close.
+ The robot performs these actions in a continuous loop until it sees the a suitable `parallel_parking` area. *See Code for Parking* for more.

### *6.5 Code for parking*

We defined our robot's code for the parallel parking system, consisting of three main parts. 

#### Step by Step

+ ****Constants and Parameters:*** First, we defined the constants and parameters we will use, including the robot's length, the required parking space length (1.25 times the robot's length), and speeds for forward and backward movements.
+ ***`measure_parking_space` function:*** It will define the continuously forward moves of the robot while using sensors to measure the distance on the right side, checking if the detected space is large enough for parking (greater than the required length). If a valid parking space is detected, the robot proceeds to execute the `parking maneuver`.
+ ***The `parallel_parking` function:*** Performs the actual maneuver: the robot first moves forward to align itself with the space, then turns to the right while moving backward to start entering the space, and finally, it turns left to straighten itself and continue reversing into the spot.
+ ***The `main_loop` function:*** Running continuously, it will check for parking spaces and initialize the `parking maneuver` once a suitable space is found. The program terminates after the robot successfully parks.
