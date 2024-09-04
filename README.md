WRO2024 ROBOTEK
====
+ Team's Name: Révine
+ Car's Name: Riska
+ Teammates: Mafer Zambrano & Isa Gonzales
+ Match Name: Robotek
  
## Team presentation

![maferZambrano](https://github.com/user-attachments/assets/aebda320-fb72-4327-8c66-aefafc43bb79)

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

## Why did we choose to participate?

We see this project as more than just a competition. It is a chance to be creative, work together, and overcome challenges—both in the design and in ourselves. By designing our robot, we are not creating just a machine but a mixture of our electronic and coding skills, and innovation.

This experience has reminded us that endorsing difficulties means finding solutions where others see problems and that we can have fun and enjoy the process. So, we thank being part of this olympiad: it has pushed us beyond the limits, broadening our minds, and, most of all, we had a great time!

## Preparing the repo

### *1. Designing the prototype*

We started by making a carton-prototype based on the turning mechanism and following the official documentation rules. This was our initial prototype:

![prototype](https://github.com/user-attachments/assets/06523245-8f3e-4c9d-9fc8-b9322338aac1)

> [!TIP]
> In order to choose the apropiate materials, we made a design and a table of components with all our options. Then, we selected the ones that seemed the most efficient to us.

![drawingPrototype](https://github.com/user-attachments/assets/8cda5ee6-cf6c-44be-bf7e-c29f5a3abca0)
![materialsSchemes](https://github.com/user-attachments/assets/58097104-9be4-432f-a44f-7228804fc0a0)

We decided to use these components:
+ ⁠Rasperrby Pi 4
+ ⁠Arduino Nano
+ Arduino Nano Expansion Shield
+ ⁠Li-Po Battery 3.7v 1000 mAh
+ ⁠TT Motor (Blue)
+ ⁠Stepper Motor 28YBJ-48
+ ⁠Driver ULN2003
+ Driver TB6612
+ Breadboard Power Supply Model Adapter Shield MB102 3.3v/5v
+ Power Bank: 5v 3A 10000 mAh
+ ⁠QTR-1A Sensors
+ ⁠IR Sensors Sharp GP2Y0A21
+ ⁠Webcam
+ Capacitor 10uF

### *2. Code for the camera*

We started by making the `detectColors.py` code for the camera. On it, we decomposed the image into pixels, which detected the color in RGB format and then converted it into a new HSV format. We used the color palette based on hue (HUE) to select the color and set the limits with which the range of colors we are looking for will be detected. Once the color code in HSV is obtained, we compared it with a specific range of values. If the desired color is within our palette, it will be highlighted with an internal frame.

### *3. Printing the prototype and ensambling*

We proceeded to print our first prototype using 3D printing. Once we had all the parts ready, we began the assembly process: we added the motors and the wheels, selected to ensure proper traction and optimal movement.  

![printed prototype](https://github.com/user-attachments/assets/dca1240a-ef3a-4b02-b663-73f74957ab60)

### *4. Code for the Raspberry PI 4*

We usedd the MicroSD card to connect to one of the computers, which we then linked to the Wi-Fi network. We configured its MicroSD card and began developing the code. This includes the modules for `motors.py`, `detectColors.py`, `ser.py`, and `main.py`.

### *5. Code for the motors*

In `motor`, we implemented the forward and backward motor functions: FORWARDS and BACKWARDS. We developed the turning logic using the step-by-step motor control (LEFT and RIGHT) and created a sequence using a 'for' loop to manage the step-by-step motor movement.

> [!NOTE]
> In the end, we decided to change the motor model to improve its efficiency. However, the code remains the same.

### *6. Code for the Arduino*

We used an Arduino Nano and developed the `analogsensor.ino` code, which, along with Sharp sensors, allowed us to measure distance from three different angles: front, left, and right. We collected the data and printed it to the serial port for monitoring. Subsequently, we connected the Arduino to the Raspberry Pi and, through the code in `ser.py`, read and processed the data provided by the sensors.

### *7. Designing and printing the second prototype*

We redesigned the prototype after realizing that we needed to adapt the new components to the cart. We 3D printed only the essential parts, such as the steering system and motor mounts, while the rest was cut from acrylic to keep the structure light and sturdy.

![printed prototype 2](https://github.com/user-attachments/assets/7b2bdaf5-1f30-4a61-9fc3-0eed9f7d6961)

### *8. Designing and printing the last prototype*

We printed the prototype for the third and final time, adding an additional level to better distribute the components and provide a mount for the webcam. We also slightly modified the design of the motor mount to fit the PowerBank, ensuring a perfect fit and a more efficient arrangement of all elements.

> [!NOTE]
> To optimize performance and extend the cart's runtime, we decided to replace the traditional batteries with LiPo cells.

![printed prototype 3](https://github.com/user-attachments/assets/7d53b3ab-7a73-4089-b90a-d9bf99f5aa0f)

### *9. Code for avoiding obstacles*


> [!NOTE]
> About the `main.py`...
