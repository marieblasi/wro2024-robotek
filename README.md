Welcome 🤩 ! 
We are Team Révine, proudly representing our country Perú 🇵🇪 🤖 !
====
<p align = "center">
  <img src = "https://github.com/user-attachments/assets/196f69c0-0233-43e6-970e-4f6ab1ee7f02">
  </p>

+ Team's Name: ***Révine***
+ Car's Name: ***Riska***
+ Teammates: ***Mafer Zambrano & Isa Gonzales***
+ Match Name: ***Robotek***

## **Table of Contents**

- [1. 🤖 About us!](#1-about-us)
  - [1.1 🌟 Team presentation](#11-team-presentation)
  - [1.2 ✅ Team Management](#12-team-management)
  - [1.3 🤔 Reasons to participate](#13-reasons-to-participate)
- [2. 🛠️ About the car](#2-about-the-car)
  - [2.1 🧠 Our autonomous car's logic](#21-our-autonomous-cars-logic)
  - [2.2 💡 Flow Diagram](#22-flow-diagram)
  - [2.3 🖥️ Why Python?](#23-why-python)
  - [2.4 🎯 Why ROS?](#24-why-ros)
- [3. ⚙️ Mobility Management](#3-mobility-management)
  - [3.1 🧱 Bill of Materials (BOM)](#31-bill-of-materials-bom)
  - [3.2 🔌 Wiring Diagram](#32-wiring-diagram)
  - [3.3 🧰 Reasons for Using Our Motors](#33-reasons-for-using-our-motors)
  - [3.4 ⚙️ Motors Axle System](#34-motors-axle-system)
  - [3.5 ⚙️ Ackermann Steering System](#35-ackermann-steering-system)
    - [3.5.1 How does the System Works](#351-how-does-the-system-works)
    - [3.5.2 Enhanced Precision](352-enhanced-precision)
- [4. 🔋 Power and Sense Management](#4-power-and-sense-management)
  - [4.1 🔌 Power Distribution Diagram](#41-power-distribution-diagram)
  - [4.2 ⚡ Power Source](#42-power-source)
    - [4.2.1 Charger](#421-charger)
  - [4.3 📷 Reasons for Using Our Sensors and Camera](#43-reasons-for-using-our-sensors-and-camera)
    - [4.3.1 STL-19P TOF Lidar](#431-stl-19p-tof-lidar)
    - [4.3.2 Monocular Camera](#432-monocular-camera)
- [5. 🏎️ Building the Robot](#5-building-the-robot)
  - [5.1 🖨️ Designing, Printing, and Ensembling](#51-designing-printing-and-ensembling)
    - [5.1.1 3D Printing Process](#511-3d-printing-process)
    - [5.1.2 The Systems](#512-the-systems)
    - [5.1.3 Camera Housing](#513-camera-housing)
    - [5.1.4 Chassis](#514-chassis)
  - [5.2 📍 Code for the Camera](#52-code-for-the-camera)
- [7. 📌 Principal Strategy](#7-principal-strategy)
  - [7.1 🔒 Open challenge](#71-open-challenge)
  - [7.2 🔒 Obstacle Challenge](#72-obstacle-challenge)
  - [7.3 🔒 Parking Strategy](#73-parking-strategy)

## 1. About us!
### 1.1 Team Presentation

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

### 1.3 Reasons to Participate
We see this project as more than just a competition. It is a chance to be creative, work together, and overcome challenges—both in the design and in ourselves. By designing our robot, we are not creating just a machine but a mixture of our electronic and coding skills, and innovation.

This experience has reminded us that endorsing difficulties means finding solutions where others see problems and that we can have fun and enjoy the process. So, we thank being part of this olympiad: it has pushed us beyond the limits, broadening our minds, and, most of all, we had a great time!

## 2. About the Car!
### 2.1 Our Autonomous Car's Logic
1. The program will begin by initializing the LIDAR sensor, the monocular camera, and the necessary variables for lap counting and timing. Once started, the car will enter a continuous loop where the main function will run repeatedly.
2. During each loop iteration, the LIDAR captures environmental data to detect walls and calculate the distance to the circuit’s boundaries. Then, the system will analyze the LIDAR data to maintain a safe distance from the black walls. If the car gets too close to a wall, it will adjust its direction and reduce speed to avoid collisions, helping it stay on course.
3. The camera and LIDAR will be used together to identify specific reference points on the circuit for lap counting. Once the car has passed the same reference point three times, it will be considered to have completed the required laps. A timer will monitor the elapsed time, adjusting speed if needed to stay within the three-minute target.
4. ***For the Obstacle Challenge***, the monocular camera will capture a visual frame to detect the color of obstacles. During these maneuvers, the LIDAR will continue to monitor the proximity to the black walls to ensure a safe evasion without colliding. Basic computer vision algorithms will analyze each frame to determine the color:
    + Red: If the obstacle is red, the car will adjust its path to pass on the right.
    + Green: If the obstacle is green, the car will adjust to the left.
5. After completing the three laps and avoiding all obstacles, the car will activate its parallel ***Parking Mode***. Using LIDAR, it will look for a suitable parking spot and, based on distance and angle calculations, perform a parallel parking maneuver.

### 2.2 Flow Diagram

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/337bbe93-56a9-46f5-a133-f05e7a8f700a">
  </p>

> [!TIP]
> You can find our Open Challenge and Obstacle Challenge diagram separately in the folder [schemes](schemes) of this repository.

### 2.3 Why Python?
Python is a widely used language, representing the best. It is used for fast and flexible development and, also, implemented for tasks that require high performance providing a solution for a system like ours, where we need to control hardware while efficiently processing data at the same time. We use it for the following advantages:
1. ***Strong language:*** Python is known for being a high-level language, easy to write and read, and excellent for rapid development, proof of concepts, and handling complex tasks such as data analysis, hardware control, and machine learning.
2. ***Management of libraries:*** This language contains a large number of easy-to-use libraries, ranging from web interface management, computer vision, and network handling to direct hardware manipulation. This allows for efficient work and rapid development of advanced functionalities without having to program them from scratch.
3. ***Use in different platforms:*** We can use Python on boards like the Raspberry Pi for general control tasks, vision, etc., where Python is commonly used because it offers extensive libraries that facilitate interaction with the operating system. 
4. ***Performance and flexibility:*** Python can be used for greater flexibility in handling advanced logic, such as data manipulation and integration with interfaces.

### 2.4 Why ROS?
ROS (Robot Operating System) is an open-source software framework designed to develop and control robots. ROS has become a standard in modern robotics due to its flexibility, modularity, and large community of developers. We use it for the following reasons: We use it for the following advantages:
 1. ***Integration of Sensors and Actuators:*** With ROS, we can easily connect and coordinate multiple sensors and actuators within a single system. This allows each component to work together seamlessly, providing our autonomous car with continuous information about its surroundings and optimizing the overall system performance.
 2. ***Environmental Perception with LiDAR:*** By using LiDAR, we obtain precise 360-degree distance data, which is essential for detecting obstacles and walls. ROS packages like `laser_scan_matcher` and `gmapping` help us process this data to create real-time maps of the environment.
 3. ***Autonomous Navigation and Path Planning:*** ROS provides us with advanced navigation tools, such as `move_base`, which allow our car to plan optimal routes and adjust them in real-time. This is particularly important for the Ostacle Challenge. With ROS, we can combine data from various sensors to make real-time decisions about the path.
 4. ***Efficient Simulation and Debugging:*** We simulate the car’s behavior in virtual environments like `Gazebo` to prevent physical damage during testing and to fine-tune our parameters. Additionally, tools like rviz let us visualize sensor data and the car’s status in real-time, which makes debugging much easier.

## 3. Mobility Management
### 3.1 Bill of Materials (BOM)
Component | Quantity | Function |
 :---: | :---: | :---: |
| Raspberry Pi 5 | 1 | A microcomputer that acts as the main brain and the **Host Controller** of the system, capable of running operating systems and handling complex processing tasks. |
| Raspberry Pi 5 Cooling Fan | 1 | A mini fan that cools the raspberry preventing it from overheating. | 
| RRC Lite Controller | 1 | Integrates several elements: ***ROS expansion board, High-Frequency PID Control, Motor Closed-Loop Control, Servo Control and Feedback, IMU Data Acquisition, Power Status Monitoring***, and a ***Power Switch***. |
| STL-19P TOF Lidar | 1 | Provides precise, 360-degree distance measurements for real-time navigation and obstacle detection in dynamic environments. |
| 15 kg.cm Digital Servo | 1 | A servo to control the Ackermann system to make precise movements. |
| 65 mm Anti-Slip Rubber Wheel | 1 | Allows the car to move back, forth, and make turns. |
| 310 DC geared Encoder Motor | 1 | A high-speed DC motor used for propelling the car. |
| Monocular Camera | 1 | A camera used for capturing images and videos, can be used for computer vision or live streaming. |
| Jumper Cables | 17 | Used to connect various components together. |
| USB Cable | 3 | A cable to connect the Raspberry Pi4 to the camera, Raspberry to Lidar, and Raspberry to Controller. |
| ⁠Li-Po Battery 7.4 V 2200 mAh 20C | 1 | A lithium polymer battery that provides portable, high-density power. |

### 3.2 Wiring Diagram

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/c9d2e663-1c4f-429b-adc3-aad25e70b846">
  </p>

### 3.3 Reasons for Using Our Motors
We selected two 310 DC Geared Encoder Motors. These motors are installed on the vehicle's rear axle, offering the torque and speed necessary for both stability and maneuverability.

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/1c9c16e2-c9d5-4682-91b8-cc7b88997cbd">
  </p>

+ ***Torque***: Each motor provides approximately 1.2 Nm of torque, which is sufficient to handle the weight and required acceleration of the vehicle. This level of torque allows the vehicle to navigate without straining the motors.
+ ***Speed***: The motors run at 450 RPM at 7.4V, giving a balance between swift response and controlled movement. This speed is ideal for applications where moderate pace and precision are essential, avoiding abrupt or excessive acceleration.

### 3.4 Motors Axle System
The two motors are connected to an axle in the rear space, which allows the wheels to support the weight of the car. This axle is essential for the car to move forward and backward efficiently, ensuring a smoother ride in curves and reducing tire wear. It improves vehicle stability, which is particularly important in tight corners or under variable road conditions.

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/ceaa0a0e-a276-4760-bf44-b892d148df29">
  </p>

### 3.5 Ackermann Steering System
Our autonomous car uses an Ackermann steering system, controlled by a 15 kg·cm digital servo, which provides precise and stable control for navigation and turns.
#### 3.5.1 How does the System Works?
The Ackermann steering geometry is designed to reduce tire slip by ensuring that all wheels align as radii of circles that share a common center when the car is turning. This configuration keeps the rear wheels fixed and places the center of rotation along a line extended from the rear axle. To achieve this geometry, the inside front wheel turns at a greater angle than the outside front wheel, allowing smoother and more efficient cornering.

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/669bde9f-9b57-4d71-b7bd-79a0b9665639">
  </p>
  
#### 3.5.2 Enhanced Precision
The high-torque digital servo enables the car to execute controlled, precise movements, making it ideal for navigating complex paths and obstacles. It allows the car to adjust its steering angle accurately and responsively, improving maneuverability and enabling smoother, more predictable turns.

## 4. Power and Sense Management
### 4.1 Power Distribution Diagram

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/8b9986c4-6b11-4f09-9e0e-405dae94d4fd">
  </p>
  
### 4.2 Power Source
The battery powering the autonomous car is a ***Lithium Polymer (Li-poly)*** type with a capacity of 2200 mAh and a nominal voltage of 7.4V. This battery was chosen specifically to meet the energy demands of the system, providing enough power to run both the Raspberry Pi and the vehicle's motors simultaneously. With a discharge capacity of 20C, the battery ensures a consistent energy supply, which is essential for maintaining system performance in high-demand applications like autonomous operation and real-time data processing.
#### 4.2.1 Charger:
The charging system for the autonomous car consists of an ***AC Charger*** specifically designed for lithium polymer (Li-poly) batteries. This charger operates at an output voltage of 7.4V and provides a steady and safe current for the 2200 mAh battery, ensuring efficient charging without overheating. The charger's design allows for a quick and secure connection to the vehicle, ensuring a full and rapid charge to keep the car's systems operating optimally.
<p align = "center">
  <img src="https://github.com/user-attachments/assets/ce21d737-9f0d-4317-855f-baacd6b274f7">
  </p>

### 4.3 Reasons for Using Our Sensors and Camera
#### 4.3.1 STL-19P TOF Lidar:
  + ***Precise environmental mapping***: With its ±10mm accuracy, the STL-19P enables precise positioning, essential for navigating narrow or intricate sections of the obstacle course. This allows our robot to make calculated movements without collisions or deviations.
  + ***Real-time obstacle avoidance***: With its fast sampling rate, the LiDAR can detect and react to obstacles dynamically, ensuring smoother movement through the course.
  + ***Enhanced performance in varied lighting***: Its high tolerance for ambient light up to 60,000 lux and ability to detect glass is essential, where lighting conditions vary. This feature ensures our robot maintains consistent performance, accurately detecting objects and avoiding potential pitfalls like transparent or shiny obstacles.

> [!IMPORTANT]
> **Placement:**
> It was positioned at an altitude of under 10 cm, so it is able to detect the walls of the path, which are also 10 cm high. This placement ensures the Lidar has a clear view of the obstacles while remaining unobstructed by other components. All other elements on the car were arranged to avoid blocking the Lidar’s line of sight.
> <img width="1206" alt="Screenshot 2024-11-10 at 18 18 03" src="https://github.com/user-attachments/assets/9e9d9df4-cfc6-4875-b832-435c4d2ebb1c">
  
#### 4.3.2 Monocular Camera:
  + ***Color detection***: Since graphical color detection is a core part of your project, the camera can precisely identify various colors on the course. This enables our robot to execute programmed actions based on specific color cues, which is crucial for the Obstacle challenge, which requires interaction with color-based objects.
  + ***Spatial awareness through data fusion***: When combining camera data with our sensor, the robot gains a richer understanding of its environment. The camera provides detailed visual context that complements other data sources, leading to a more informed and adaptable navigation strategy.

> [!IMPORTANT]
> **Placement:**
> It was located at the front of the car, providing a front-facing view from the car and enhancing the car's ability to detect and classify obstacles by color.  This location allows the camera to complement the Lidar without interference, capturing detailed visual information about the obstacles.
> <img width="1049" alt="Screenshot 2024-11-10 at 18 17 18" src="https://github.com/user-attachments/assets/198d3541-ec12-4232-97b8-b4fb0fde5850">


## 5. Building the Robot
This autonomous car project features a carefully constructed design that combines metal components with custom 3D-printed parts to create a durable, lightweight, and functional structure.
### 5.1 Designing, Printing, and Ensembling
#### 5.1.1 3D Printing Process
Custom parts, such as axles, gears, and component supports, were fabricated using 3D printing. This allowed for complex designs tailored to the specific layout and functionality required for the car’s systems. The flexibility of 3D printing enabled rapid prototyping, where parts were tested, refined, and adjusted to ensure compatibility and strength. This process helped achieve precise fits for components like motor mounts and sensor housings, enhancing overall performance and structural integrity.

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/52a1f066-d80e-4882-8f03-1a08d98fd786">
  </p>

#### 5.1.2 The Systems
The mobility and steering systems include motors, axles, gears, and a high-torque digital servo for precise control. The motor and servo systems were mounted to maximize power application to the wheels, while axles and gears were aligned to handle torque efficiently.

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/491afc7a-acc9-4157-94f5-fc91b3eca43d">
  </p>

#### 5.1.3 Camera Housing
The monocular camera is mounted at the front of the car in a dedicated 3D-printed housing to capture clear, direct images of the path ahead. This mount places the camera at an ideal angle and height, ensuring that it detects obstacles and recognizes colors effectively. The camera mount is also aligned to avoid interference with the LiDAR sensor’s field of view, maximizing the sensing range of both components.

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/08a7b2f7-d6ce-41b6-a408-0eb419dda3bb">
  </p>

#### 5.1.4 Chassis
The base and upper casing were crafted from aluminum to provide strength and lightweight support for all components. The base was designed to securely mount the Raspberry Pi and support the weight of the vehicle’s systems, offering a stable foundation and balanced weight distribution critical for stability. The upper casing, which houses the LiDAR sensor, was designed to ensure the sensor has an unobstructed view while protecting it from potential impacts and environmental factors.

<p align = "center">
  <img src = "https://github.com/user-attachments/assets/b878388c-313e-4fd7-aca1-75f875a06fa5">
  </p>

### 5.2 Code for the Camera

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
+ ***Webcam initialization and color setup:*** The program initialized the webcam using `cv2.VideoCapture(1)` to capture live video. It defined two colors, `red` and `green`, in `BGR` format, which was used for detecting those specific colors within the video feed.
+ ***Main Loop with frame capture:*** The program will continuously capture frames from the webcam. Each frame was converted from `BGR` to `HSV` format, which allowed more effective color-based filtering. The frame was then processed to isolate the areas that match the target color using the previously calculated `HSV` limits. If a match is found, a rectangle is drawn around the detected color in the frame, which is then displayed in a window as shown:

<p align = "center">
  <img width="900" alt="colorDetection" src="https://github.com/user-attachments/assets/fcd87a76-d15e-44bb-84c2-3114a56d85bc">
</p>

## 6. Assembly Instructions

<p align = "center">
  <img src="https://github.com/user-attachments/assets/59f47ae4-5441-4511-bcb8-1ff3889bf402">
</p>

+ ***Base Assembly.***
+ ***Raspberry Placement:*** Begin by securing the Raspberry Pi to the center of the base with 4 mounts, using screws to keep it stable.
+ ***Install the motor system at the rear of the base:*** Motor supports are screwed into the base. Each motor is attached to its support with screws, ensuring alignment. Attach the gears to each motor shaft. Insert the axle between the two motors, secured with two side supports attached to the base. The base edges help to hold the axle in place.
+ ***Ackermann System:*** In the front of the base, install the Ackermann steering system. Secure the system with screws. Mount the servo motor in its housing and attach it to the Ackermann mechanism.
+ ***Upper Casing Assembly:*** Attach 4 mounts at the corners of the base to support the upper casing.

<p align = "center">
  <img src="https://github.com/user-attachments/assets/d8bbc8ef-fb9c-45cf-954c-44c064641d15">
</p>

+ ***LiDAR Placement:*** Screw the LiDAR sensor into a central location on the upper casing. Attach the LiDAR adapter at the front, ensuring it does not obstruct the view of other components.
+ ***LiPo Battery Placement:*** Place the LiPo battery at the rear of the upper casing, ensuring it does not interfere with the LiDAR’s field of view.
+ ***Camera Placement:*** Place the monocular camera on the front of the base, positioning it to capture obstacles and detect colors in the car's path. Secure the camera using its dedicated 3D-printed mount, ensuring it does not obstruct the LiDAR's view or other sensors.

After completing the mechanical assembly, connect all electronic components according to the provided wiring diagram. Follow the wiring carefully to ensure proper function of the motor, LiDAR, and servo systems. You can see the Wiring diagram in the folder [schemes](schemes).

## 7. Principal Strategy
### 7.1 Open challenge

<p align = "center">
  <img src="https://github.com/user-attachments/assets/49088091-f8d1-4cc6-a4a1-3171e5891f55">
  </p>

We configured the LiDAR system to enable precise measurement of the distances between the vehicle and surrounding walls. The primary function of the LiDAR is to assess the spatial environment continuously; in instances where no walls or corners are detected, the system defaults to a command that propels the vehicle forward. Upon detecting a wall or other obstruction, the LiDAR re-evaluates the vehicle's position and, based on this new spatial data, recalculates whether there is adequate space for continued movement in the desired direction. When a corner is identified, the vehicle initiates a turning maneuver and begins tracking lap progression. This setup allows for efficient navigation and accurate lap counting through environmental feedback loops.

<p align = "center">
  <img src="https://github.com/user-attachments/assets/53aa9164-74f9-4000-afcc-756a9ed1612e">
  </p>

### 7.2 Obstacle Challenge
The monocular camera is programmed to analyze the color of pillars within the vehicle's path. Upon detecting a red-colored pillar, the system will direct the vehicle to steer right, whereas a green-colored pillar prompts a leftward maneuver. Following the color-based directional adjustment, the vehicle recalibrates its path to ensure alignment with the pre-established navigation loop. This sequence allows the vehicle to dynamically integrate real-time visual data with its primary navigation loop, enhancing responsiveness to environmental cues.

<p align = "center">
  <img src="https://github.com/user-attachments/assets/92544ffe-bac1-489a-9a5f-db740bb29ac1">
</p>

### 7.3 Parking Strategy
Upon completing the three laps, the vehicle initiates a Parking Sequence, beginning with the detection of the parking boundaries through LiDAR analysis. The LiDAR system assesses the available space and aligns the vehicle with the detected parking area. If sufficient space is confirmed, the vehicle executes a parallel parking maneuver. Following this, the system verifies the vehicle’s final position to ensure proper alignment, at which point it halts. In cases where space is insufficient, the vehicle adjusts its orientation and resumes scanning to locate an appropriate parking area, repeating the process until successful parking is achieved.

<p align = "center">
  <img src="https://github.com/user-attachments/assets/e138885a-3f35-4f6f-b869-38107b6f0949">
</p>
