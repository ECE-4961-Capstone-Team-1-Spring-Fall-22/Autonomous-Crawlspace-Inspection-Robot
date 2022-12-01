## Navigation Code

# What does the software do? 

This python script is a combination of navigation/movement, imaging, and environmental sensing communication protocols. This program uses USB serial communication to talk to four Arduinos (3 for environmental sensing and 1 for movement), collects data from the ultrasonic sensors for path planning, and captures images from the HD cameras.  

# Dependencies 

This program requires installing the Arduino IDE onto the Raspberry Pi 4B. This program requires that python 3.7 and pip be installed onto the Raspberry Pi 4B. Additionally, this program requires the following python packages to be installed for use: RPI.GPIO, serial, threading, NumPy, and OpenCV.  

# How to Install? 

To install the previously mentioned dependencies, enter the bellow commands into the Ubuntu terminal on the Raspberry Pi 4B.  

sudo apt update 

sudo apt upgrade 

sudo apt install python3.7 

python –version 

sudo apt-get -y install python3-pip 

sudo apt-get install rpi.gpio 

sudo apt-get install time 

sudo apt-get install pyserial 

sudo apt-get install multithreading 

sudo apt-get install python3-opencv 

pip3 install numpy 

# How to Run? 

To run this program, open a new command terminal. In the command terminal, type “Arduino”. The Arduino IDE is used to identify which USB ports the four Arduinos are connected to. Once the proper USB ports are identified, change the USB variables in lines 12-15 from “ACMn” to the appropriate USB port. Next, open another command terminal and enter the following (note: the file path for the code is everything BEFORE /Combined_Code.py…edit accordingly): 

Python /home/ubuntu/Desktop/ECE_4961_4971_Autonomous_Crawlspace_Inspection_Robot/Combined_Code.py 
