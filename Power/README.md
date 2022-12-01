# Autonomous-Crawlspace-Inspection-Robot
This branch documents the design process for the power subsytem. 

# Specs, Design, and Analysis: 
This system had the following requirements
* Provide +5V power to the logic electronics and microcontrollers
* Provide +12V power to the motor and mechanical system
* Prevent surges from creating system-wide failures
* Filter inconsistencies from the battery supply voltage and provide steady DC voltage to the components

The design of the system involved custom buck converters which allowed the use of both +12V and +5V power.
Fuses were used to ensure that power surges from one component would not negatively impact the other subsystems.
Terminal blocks were also used for their secure connections and ability to disconnect if changes were made. 

Analysis for the system can be found in the experimental data file.
