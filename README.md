# Autonomous-Crawlspace-Inspection-Robot
This GitHub contains all relevant files used during development. For a comprehensive guide to the repository set up see the bottom of the document.
## Executive Summary
Crawl spaces grant convenient access to the plumbing, duct work, and electrical wiring of a house, but they often present unique dangers to maintenance professionals and residents alike. Exposure to harsh breathing conditions, hanging obstacles, uncomfortable working positions, and even animals can cause non-ideal conditions. This capstone project will focus on the design and assembly of a robot prototype that can perform these inspections autonomously. The end product will be an autonomous, mobile robot that can be left unattended in a crawlspace by an inspector. It will navigate through the space, create a map and model of the space, compile an image of the entire crawlspace ceiling, and collect sensor data. This sensor data will include humidity, temperature, and wood moisture content.

## Current Robot Capabilities
The first iteration of the project focused on setting up the hardware systems. Sensors, microcontrollers, motors, and power circuits were designed and implemented as part of a larger multi-group project. The following details the current capabilities of the robot.

* Low-level autonomy which allows the robot to navigate through an enclosed area
* Creating a map of the area using the SLAM algorithm
* Take pictures throughout an area and stitch simple areas into a singular, larger image
* Collect humidity, temperature, and moisture content data and overlay information on images
* Supply power for consistent operation across all components
* Robot movement through serial commands and return encoder data to the main microcontroller
* Manual control through text-based commands while also streaming live video to the operator

For more detail on current designs, see files in sub-system directories

## Salient Outcomes
Although this project includes lofty long-term goals, many exceptional systems were able to be incorporated in the first iteration of the project.
* The mapping was found to be accurate to 93% or more in each test that was run. While this is useful information for an inspector to have, it will also provide an invaluable framework for future updates to the autonomy
* Power was successfully applied to all parts of the system with no over-currents or under-voltages experienced by the system. All back EMF from the motors was successfully filtered out as well.
* Environmental sensing was found to be exceptionally accurate. Temperature and Humidity were both found to be 96% accurate or greater while moisture content was successfully measured to within 2.5% moisture.

## Pictures and Videos
The final system demo in the crawlspace can be found [here](https://www.youtube.com/watch?v=mYopD1X_bd8&t=9s)

A picture of the final system can also be found below 

![alt text]( https://github.com/ECE-4961-Capstone-Team-1-Spring-Fall-22/Autonomous-Crawlspace-Inspection-Robot/blob/main/Pictures%20and%20Videos/Croomba_Final_Image.PNG)

## Who Are We? Mr. Jesse Robert's ECE 4961 Capstone Team 1

* James (Jim) Camp - Senior Electrical Engineering Major, Mechatronics Concentration - Environmental Sensor Subsystem Developer - Delegator 
* John-Caleb (JC) Williams - Senior Electrical Engineering Major, Electromagnetics Concentration - Navigation Subsystem Developer - Treasurer
* John Harris - Senior Electrical Engineering Major, Controls Concentration - Power Subsystem Developer - Secretary
* Joseph Thomas - Senior Electrical Engineering Major, Power Concentration - Movement Subsystem Developer - Social 

* Mr. Jesse Roberts - Professor and Faculty Advisor

* Project Stakeholders - This project was developed for anyone who needs to inspect their crawlspace. This includes homeowners, building inspectors, and renovators. The system is also a great solution for anyone experiencing issues with mold or unsafe crawlspace conditions.

# Repo Guide
This repository contains the entirety of the Autonomous Crawlspace Inspection Robot’s REV1 design files. The folder breakdown is as follows
* Design Files – Contains files that represent the final design state of the project. This is made up of an overall system schematic and the bill of materials (BOM).
* Documentation – Contains all written submissions created throughout both semesters of the course. Also included are the presentations used at the end of the project.
* Environmental Sensing – This subsystem is responsible for the data collection which occurs throughout the crawlspace. Additionally, image stitching is also included within this folder.
* Movement – This subsystem is responsible for controlling the physical motion and positioning of the robot. 
* Navigation – This system handles the mapping and autonomy. Interfacing with the Raspberry Pi, LIDAR, distance sensors, and remote access are also included in this subsystem.
* Pictures and Videos – A repository for all the pictures and videos taken throughout the experimentation and testing.
* Power - This subsystem is responsible for providing continuous power to all the components. Circuit protection and power filtering are also integrated into this subsystem.

