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

- [1. 🤖 About us!](#1-about-us)
  - [1.1 🌟 Team presentation](#11-team-presentation)
  - [1.2 ✅ Team Management](#12-team-management)
  - [1.3 🤔 Why did we choose to participate?](#13-why-did-we-choose-to-participate)
- [2. 🛠️ About the car](#2-about-the-car)
  - [2.1 💡 Which is our autonomous car's logic?](#21-which-is-our-autonomous-cars-logic)
  - [2.2 ⚡ Flow Diagram](#22-flow-diagram)
  - [2.3 🖥️ Why Python?](#23-why-python)
  - [2.4 🔌 Why ROS?](#24-why-ros)
- [3. Mobility Management](#3-mobility-management)
  - [3.1 Bill of Materials (BOM)](#31-bill-of-materials-bom)
  - [3.2 Wiring Diagram](#32-wiring-diagram)
  - [3.3 Differential System](#33-differential-system)
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

|  | 🐨 🤖 🥐 🌟 🥋 🎨 🎼 🥧 🍀 | 🥇 🧑‍🚀 🦢 🏛️ 🎧 🏎️ 🏁 🚀 🌙 🔭 |
| :---: | :---: | :---: |
| **Name** | Isabella Gonzales | Maria Fernanda Zambrano |
| **Age** | 15 | 17 |
| **Role** | Electronics and Technical Designer | Programming and Technical Analyst |
| **Extra** | I love music (singing and playing the guitar), making origami, and painting. A fun fact about me is that I sang in the National Theather wearing pijamas when I was 6. | Some of my hobbies are swimming, reading, and playing instruments. A fun fact about me is that I am a huge F1 fan! |

### 1.2 Team Management

Our project is the product of a collaborative effort by a talented and dedicated team, with each member contributing their unique expertise. As students of Robotek from Lima, Peru, we have learned valuable skills in robotics and technology. 

+ ***Team Supervisor:*** Alejandro Garayar
+ ***Coach:*** Renzo Damian

### 1.3 Why did we choose to participate?

We see this project as more than just a competition. It is a chance to be creative, work together, and overcome challenges—both in the design and in ourselves. By designing our robot, we are not creating just a machine but a mixture of our electronic and coding skills, and innovation.

This experience has reminded us that endorsing difficulties means finding solutions where others see problems and that we can have fun and enjoy the process. So, we thank being part of this olympiad: it has pushed us beyond the limits, broadening our minds, and, most of all, we had a great time!

## 2. About the car!

### 2.1 Which is our autonomous car's logic?

1. The program will begin with the initialization of sensors, camera, and variables. Once started, the car will enter a continuous loop with the main function running endlessly. In each loop iteration, *it will capture a frame from the camera and will read input from various sensors*, including distance and reflectance sensors.
2. The captured frame  is then analyzed to detect obstacles, and if one is found, its color is identified as either red or green. *The navigation strategy adjusts the car to pass on the right side for red obstacles and on the left side for green ones.* Steering adjustments are combined with the obstacle avoidance strategy to manage the car’s movement. The system also monitors proximity to obstacles, performing avoidance maneuvers if too close, reducing speed when necessary, or maintaining normal speed otherwise.
3. The car moves forward based on the calculated steering and speed. *Reflectance sensors are used to count the number of laps completed.* If all required laps are finished, the car navigates to the parking area and performs parallel parking; if not, the loop continues. Finally, the program ends after successful parking or if interrupted.

### 2.2 Flow Diagram


### 2.3 Why Python?

Python is a widely used language, representing the best. It is used for fast and flexible development and, also, implemented for tasks that require high performance providing a solution for a system like ours, where we need to control hardware while efficiently processing data at the same time.

1. ***Complementing the strengths of both languages:*** Python is known for being a high-level language, easy to write and read, and excellent for rapid development, proof of concepts, and handling complex tasks such as data analysis, hardware control, and machine learning.
2. ***Management of libraries:*** This language contains a large number of easy-to-use libraries, ranging from web interface management, computer vision, and network handling to direct hardware manipulation. This allows for efficient work and rapid development of advanced functionalities without having to program them from scratch.
3. ***Use in different platforms:*** We can use Python on boards like the Raspberry Pi for general control tasks, vision, etc., where Python is commonly used because it offers extensive libraries that facilitate interaction with the operating system. 
4. ***Performance and flexibility:*** Python can be used for greater flexibility in handling advanced logic, such as data manipulation and integration with interfaces.

### 2.4 Why ROS?

## 3. Mobility Management

### 3.1 Bill of materials (BOM)
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

### 3.2 Wiring diagram

## 4. Power and Sense Management

### 4.1 Reasons for choosing our sensors and camera

+ STL-19P TOF Lidar:

  + ***Precise environmental mapping***: With its ±10mm accuracy, the STL-19P enables precise positioning, essential for navigating narrow or intricate sections of the obstacle course. This allows our robot to make calculated movements without collisions or deviations.
  + ***Real-time obstacle avoidance***: With its fast sampling rate, the LiDAR can detect and react to obstacles dynamically, ensuring smoother movement through the course.
  + ***Enhanced performance in varied lighting***: Its high tolerance for ambient light up to 60,000 lux and ability to detect glass is essential, where lighting conditions vary. This feature ensures our robot maintains consistent performance, accurately detecting objects and avoiding potential pitfalls like transparent or shiny obstacles.

+ Monocular Camera:

  + ***Color detection***: Since graphical color detection is a core part of your project, the camera can precisely identify various colors on the course. This enables our robot to execute programmed actions based on specific color cues, which is crucial for the Obstacle challenge, which requires interaction with color-based objects.
  + ***Spatial awareness through data fusion***: When combining camera data with our sensor, the robot gains a richer understanding of its environment. The camera provides detailed visual context that complements other data sources, leading to a more informed and adaptable navigation strategy.

### 4.2 Power distribution diagram



## Building the Robot
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

### *4.2 Designing, Printing, and Ensembling*

What we changed:
+ Added an additional level to better distribute the components and provide a mount for the webcam.
+ Slightly modified the design of the motor mount to fit the PowerBank 12000mAh, ensuring a perfect fit and a more efficient arrangement of all elements.
+ Added 2 QRT 1A Sensors to improve the precision of environmental sensing while a MPU6050 Accelerometer & Gyroscope Sensor was included to enhance stability and orientation control.
+ Changed the engine and adjusted the Gear ratio to provide better torque for handling challenging terrain.
+ After, upgrading our batteries to LiPo cells to increase power capacity and efficiency, a camera was mounted for real-time visual feedback, and a push button, for easy interaction.
+ Change the metal wheels to plastic ones for their lightweight properties, and the front wheels’ support was reinforced with ball bearings to reduce friction and ensure smoother movement.

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/dca1240a-ef3a-4b02-b663-73f74957ab60", width = "650px">
  </p>

### *4.3 Code for the Raspberry PI 4*

### *4.4 Code for the motors*
  
### *6.3 Main code* 

### *6.4 Code for avoiding obstacles*

### *6.5 Code for parking*
