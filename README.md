Welcome! We are Team Révine representing our country... Perú! 🇵🇪🤖
====

![robotek](https://github.com/user-attachments/assets/d41e4236-aab7-4a30-a2f4-86d483993c72)

+ Team's Name: ***Révine***
+ Car's Name: ***Riska***
+ Teammates: ***Mafer Zambrano & Isa Gonzales***
+ Match Name: ***Robotek***
  
## About us!

### 1.1 Team presentation

![mafer phto](https://github.com/user-attachments/assets/a4aac382-f16b-45c4-b467-26af949a7d07)

---
### *Maria Fernanda Zambrano*
🥈 🧑‍🚀 🦢 🏛️ 🎧 🏎️ 🏁 🚀 🌙 🔭 

Age: 17

Hi! My name is Mafer and I am from Peru. Some of my hobbies are swimming, reading, and playing instruments. A fun fact about me is that I am a huge F1 fan!

---
![isaGonzales](https://github.com/user-attachments/assets/0ae75f01-ae9e-49fe-a418-98b065694f57)

### *Isabella Gonzales*
🐨 🤖 🥐 🌟 🥋 🎨 🎼 🥧 🍀

Age: 15

Hello! 
My name is Isa and I am from Peru. 
I love music (singing and playing the guitar), making origami, and painting. 
A fun fact about me is that I sang in the National Theather wearing pijamas when I was 6.

### 1.2 Team Management

Our project is the product of a collaborative effort by a talented and dedicated team, with each member contributing their unique expertise. As students of Robotek from Lima, Peru, we have learned valuable skills in robotics and technology. To learn more about our history and participations, follow us on [Instagram](https://www.instagram.com/ro_bo_tek?igsh=MXZydWFtamlzbHd4ag==).

+ ***Team Supervisor:*** 
+ ***Coach:***

### 1.3 Why did we choose to participate?

We see this project as more than just a competition. It is a chance to be creative, work together, and overcome challenges—both in the design and in ourselves. By designing our robot, we are not creating just a machine but a mixture of our electronic and coding skills, and innovation.

This experience has reminded us that endorsing difficulties means finding solutions where others see problems and that we can have fun and enjoy the process. So, we thank being part of this olympiad: it has pushed us beyond the limits, broadening our minds, and, most of all, we had a great time!

### 1.4 Why Python and C++?

Python and C++ are two widely used languages, representing the best of both worlds. While one is used for fast and flexible development, the other can be implemented for tasks that require high performance. However, together they provide a solution for a system like ours, where we need to control hardware while efficiently processing data at the same time.

1. ***Complementing the strengths of both languages:*** Python is known for being a high-level language, easy to write and read, and excellent for rapid development, proof of concepts, and handling complex tasks such as data analysis, hardware control, and machine learning. C++, on the other hand, is highly efficient in terms of speed and optimization, making it ideal for performance-critical tasks like real-time sensor handling and signal processing.
2. ***Management of libraries:*** Both languages contain a large number of easy-to-use libraries, ranging from web interface management, computer vision, and network handling to direct hardware manipulation. This allows for efficient work and rapid development of advanced functionalities without having to program them from scratch.
3. ***Use in different platforms:*** We can use Python on boards like the Raspberry Pi for general control tasks, vision, etc., where Python is commonly used because it offers extensive libraries that facilitate interaction with the operating system. In the case of C++, it will be used on Arduino. Microcontrollers like the one we will use are typically programmed in C++ because this language allows for more precise control, lower memory usage, and lower latency, which is essential when working with limited resources and tasks that require high efficiency, such as handling sensors in real time.
4. ***Performance and flexibility:*** C++ for better performance, such as sensor reading and processing; and Python for greater flexibility in handling advanced logic, such as data manipulation and integration with interfaces. This way, the versatility and communication of both libraries are fully leveraged.   

## 2. Our road to success!

### *2.1 Designing the prototype*

We started by making a carton-prototype based on the turning mechanism and following the official documentation rules. This was our initial prototype:

![prototype](https://github.com/user-attachments/assets/06523245-8f3e-4c9d-9fc8-b9322338aac1)

> [!TIP]
> In order to choose the apropiate materials, we made a design and a table of components with all our options. Then, we selected the ones that seemed the most efficient to us.

![drawingPrototype](https://github.com/user-attachments/assets/8cda5ee6-cf6c-44be-bf7e-c29f5a3abca0)
![materialsSchemes](https://github.com/user-attachments/assets/58097104-9be4-432f-a44f-7228804fc0a0)

We decided to use these components:

| Component | Quantity | Function |
| :---: | :---: | --- |
| ⁠Raspberry Pi 4 | 1 | A microcomputer that acts as the main brain of the system, capable of running operating systems and handling complex processing tasks. |
| Arduino Nano | 1 | A compact microcontroller used for control tasks and processing sensor signals. |
| Arduino Nano Expansion Shield | 1 | An expansion board for the Arduino Nano that facilitates the connection of various modules and sensors. |
| ⁠Li-Po Battery 3.7v 1000 mAh | 2 | A lithium polymer battery that provides portable, high-density power. |
| NovaMax Motor 800 Rpm | 1 | A high-speed DC motor used for propelling the cart |
| Stepper Motor 28YBJ-48 | 1 | A stepper motor used for precise movements, ideal for position control applications. |
| Driver ULN2003 | 1 | A motor driver for the stepper motor, providing the necessary current for its operation. |
| Driver TB6612 | 1 | A DC motor driver that allows efficient control of motors using control signals. | 
| Breadboard Power Supply Model Adapter Shield MB102 3.3v/5v | 1 | A regulated power supply for breadboards, providing 3.3V and 5V voltages. |
| Power Bank: 5v 3A 10000 mAh | 1 | A portable power source used to power the Raspberry Pi and other components. | 
| QTR-1A Sensors | 1 | IR reflection sensors used to detect the presence or absence of nearby objects. |
| ⁠IR Sensors Sharp GP2Y0A21 | 3 | An IR distance sensor that measures the distance of nearby objects using an infrared beam. | 
| ⁠Webcam | 1 | A camera used for capturing images and videos, can be used for computer vision or live streaming. |
| Capacitor 10uF | 1 | An electronic component used to store charge and smooth out voltage fluctuations. | 

### *2.2 Code for the camera*

We started by making the `detectColors.py` code for the camera. On it, we decomposed the image into pixels, which detected the color in RGB format and then converted it into a new HSV format. We used the color palette based on hue (HUE) to select the color and set the limits with which the range of colors we are looking for will be detected. Once the color code in HSV is obtained, we compared it with a specific range of values. If the desired color is within our palette, it will be highlighted with an internal frame.

<img width="1052" alt="colorDetection" src="https://github.com/user-attachments/assets/fcd87a76-d15e-44bb-84c2-3114a56d85bc">


### *2.3 Printing the prototype and ensambling*

We proceeded to print our first prototype using 3D printing. Once we had all the parts ready, we began the assembly process: we added the motors and the wheels, selected to ensure proper traction and optimal movement.  

![printed prototype](https://github.com/user-attachments/assets/dca1240a-ef3a-4b02-b663-73f74957ab60)

### *2.4 Code for the Raspberry PI 4*

We usedd the MicroSD card to connect to one of the computers, which we then linked to the Wi-Fi network. We configured its MicroSD card and began developing the code. This includes the modules for `motor.py`, `detectColors.py`, `ser.py`, and `main.py`.

### *2.5 Code for the motors*

In `motor.py`, we implemented the forward and backward motor functions: FORWARDS and BACKWARDS. We developed the turning logic using the Stepper motor control (LEFT and RIGHT) and created a sequence using a 'for' loop to manage the Stepper motor movement.

> [!NOTE]
> In the end, we decided to change the motor model to improve its efficiency. However, the code remains the same.

### *2.6 Code for the Arduino*

We used an Arduino Nano and developed the `analogsensor.ino` code, which, along with Sharp sensors, allowed us to measure distance from three different angles: front, left, and right. We collected the data and printed it to the serial port for monitoring. Subsequently, we connected the Arduino to the Raspberry Pi and, through the code in `ser.py`, read and processed the data provided by the sensors.

### *2.7 Designing and printing the second prototype*

We redesigned the prototype after realizing that we needed to adapt the new components to the cart. We 3D printed only the essential parts, such as the steering system and motor mounts, while the rest was cut from acrylic to keep the structure light and sturdy.

![printed prototype 2](https://github.com/user-attachments/assets/7b2bdaf5-1f30-4a61-9fc3-0eed9f7d6961)

### *2.8 Designing and printing the last prototype*

We printed the prototype for the third and final time, adding an additional level to better distribute the components and provide a mount for the webcam. We also slightly modified the design of the motor mount to fit the PowerBank, ensuring a perfect fit and a more efficient arrangement of all elements.

> [!NOTE]
> To optimize performance and extend the cart's runtime, we decided to replace the traditional batteries with LiPo cells.

![printed prototype 3](https://github.com/user-attachments/assets/7d53b3ab-7a73-4089-b90a-d9bf99f5aa0f)

### *2.9 Code for avoiding obstacles*

> [!NOTE]
> About the `main.py`...

### *2.10 Code for the turns*


### *2.11 Code for parking*
