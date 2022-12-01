# Enviromental Sensing System


## Specs, Design, and Analysis:
This system is designed to collect 3 types of sensor data while also taking pictures of the crawlspace ceiling. The sensor data consists of the following
* Humidity
* Temperature 
* Wood moisture content

The humidity and temperature system consits of prebuilt sensors which interface with Arduino microcontrollers. However, the mositure content probe had to be custom built. It was made by creating a voltage divider that can switch the value of R1 depending on the range needed to measure. These three sensors each used their own microcontroller to maintain modularity.

A board stack was deisgned to allow for simple interfacing between the sensor modules. This works by using 3 PCBs which are sized the same and can be mounted on top of each other using 1 inch tall standoffs. The power connections for each board are passed throughout the staack using header pins with a long tail. This also allows for any new sensors to be snapped on top of the existing sensors and easily added to the system.

The final part of this subsystem is the image collection. Pictures are taken throughout operation and associated to a set of sensor data. The moisture content is displayed on each picture before being stitched together. Temperature and humidity are treated as an array and have the averages and standard deviations calculated. These values are then used to determine if any outliers exist and dispaly the location of these outliers on the images.

This README file constitutes a summary, for detailed design information and analysis of each component see signoff files in this repository.
A seperate README exists for the software in the relevant sub-directory.
