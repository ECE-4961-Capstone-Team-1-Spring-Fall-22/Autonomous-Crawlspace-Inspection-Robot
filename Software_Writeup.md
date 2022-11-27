# Software Writeup
More detailed software descriptions can be found in the individual subsystem folders. Below is a high-level breakdown of the various software that is integrated into the system

## Navigation
* Autonomy
- Simple autonomy allows the robot to bounce around a space wihtout getting stuck
- Manual control is available through the command terminal in case of failure
* Mapping
- Robot Operating System (ROS) was used along with the SLAM algorithm to create a map
- This map can be visualized in RViz 
* Imaging
- The robot takes images of the ceiling at set intervals as it naviagtes
- These images are stitched together to create a wholistic view of the ceiling
- Live video is also streamed to a remote desktop in case of autonomy failure

## Enviromental Sensing
* Three programs were written for this system, one for each sensor
* The humidity and temperature programs required very simple code
- Programs recieved data from their respective sensors
- Data was sent to the main microcontroller through serial communication
* The moisture content probe took a resistance measurement
- This was done by switching through various R1 values in a voltage divider
- The final resistance value is converted to a moisture content and sent to the main microcontroller through serial communication

## Mechanical Movement
* An Arduino Mega handles the program which controls the motors
* Commands are sent from the main microcontroller to set the motor direction
* Encoder data is sent back to the Mega and Raspberry Pi so that the speed and position can be known

## Power
* No programming was necessary for the power system because it was purely hardware
