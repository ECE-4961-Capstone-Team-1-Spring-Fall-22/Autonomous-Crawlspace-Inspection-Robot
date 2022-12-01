# Navigation Subsystem 

## Specs, Design, and Analysis: 

This system is designed to use LiDAR and Ultrasonic distance sensors to navigate the inspection robot throughout a model crawl space while creating a detailed map of the surrounding environment. Additionally, the Navigation Subsystem handles USB communication with Arduino Mega/Nanos included in the Movement and Environmental Sensing Subsystems. The Navigation Subsystem MCU, sensors, wireless access point, and imaging hardware were chosen as hardware components capable of processing graphical heavy processing loads, complex distance measurements, and long-range communication protocols.  

The main MCU was required to run Ubuntu 20.04, the Robot Operating System (ROS), and visually heavy programs such as RVIZ and Gazebo. The 4 GB Raspberry Pi 4B was chosen for the Navigation Subsystem, as the CPU speed and RAM size were thought to be plenty for any computational needs. 

The distance sensors were needed to supply Python and ROS with exact and meaningful distance measurements that could be used to effectively guide the inspection robot throughout the crawl space. Moving at roughly 1 foot per second, the distance sensors were only required to supply 2 samples/second (via the Nyquist Theorem). The 360 Degree Slamtec RPLiDAR was chosen due to its high sampling frequency (KHz range), modularity, and readily available python based packages. The SeeedStudio Grove Ultrasonic Sensor was chosen due to the sensor output voltage of 3.3 Volts (maximum RPI GPIO Pin Voltage) and the included noise-filter for distance measurements.  

The wireless access point was needed to supply either a 2.4 or 5 GHZ wireless network, per FCC communication regulations. Additionally, the wireless access point (WAP) needed to supply a minimum communication range of at least 70 feet and a transmission speed of at least 100 mbps. The TP-Link N300 was chosen due to its maximum wireless transmission speed of 300 mpbs and its size, modularity, and power requirements (5 Volt 1 Amp).  

The camera was needed to provide detailed 720p or 1080p images and live video-feed for manual operation of the inspection robot. Additionally, the camera needed to be equipped with a medium/wide angle lens for capturing a large amount of information in the image of the crawl space ceiling. The camera also needed to be lit by a LED light so that the images would have enough illumination for post-processing and analysis. The SVPro 60 Degree HD USB Camera was selected for the imaging hardware due to its capability for high resolution images and fast autofocus. The Voltaic LED USB Emergency Light was chosen as the lighting hardware due to its modularity, size, light intensity, and power requirements (5 Volts 400 milliAmps).  

## Navigation Subsystem Components

Raspberry Pi 4B 4GB (Main MCU) 

Slamtec 360 Degree LiDAR (Distance Sensor) 

SeeedStudio Grove Ultrasonic Sensors (Distance Sensor) 

TP-Link N300 Travel Router (Wireless Access Point) 

SVPro HD USB 1080p Cameras (Ceiling/Wall Visual Capture Device) 

Voltaic USB LED Emergency Light (Camera Illumination) 

The “Software” folder contains the Navigation Python script used to navigate throughout the crawl space, communicate with the Movement Subsystem Arduino, and take images of the crawl space ceiling. Also, this script allows the user to see live video-feed from the wall-oriented HD Camera if manual control is needed.  

The “Signoff” folder contains research, analysis, and validation of the chosen components  adherence to given constraints and specifications of the Navigation Subsystem.  

The “Schematic” folder contains a detailed KiCAD schematic of the Navigation Subsystem.  
