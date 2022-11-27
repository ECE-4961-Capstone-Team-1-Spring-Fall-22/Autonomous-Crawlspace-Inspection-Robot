# Navigation Subsystem

## Specs, Design, and Analysis:

This system was required to record and analyze data from Lidar, IR, and Ultrasonic sensors in order to determine navigation and movement instructions for the Autonomous Crawl Space Inspection Robot. 
Additionally, this system was required to provide images of the crawl space for operators and homeowners while laying a foundation for manual control with live video feed in the case that the robot is in need of assistance. 

To adhere to these requirements, a system was developed where each navigation sensor returns data to the Raspberry Pi, via usb connections or GPIO connections. 
The Raspberry Pi will then input the data collected from the sensors to the robot operating system (ROS) software and utilize various libraries in order to determine the navigation protocols. 

Circuit analysis as well as calculations that were performed to verify each portion of this subsystem are included. 

This README file constitutes a summary for detailed design information and analysis of each component see signoff files in this repository.  
