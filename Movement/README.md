# Mechanical Movement System
The mechanical movement subsystem is essential for the operation 
of the Autonomous Crawlspace Inpsection Robot. The main purpose
of this system is to provide the robot with the ability to move.

# Specs, Design, and Analysis: 
This system has been designed to:

Communicate with the Navigation System where it receives directional instructions and sends back an instantaneous speed

Fit within the 16 inch height constraint and house all the hardware

Allow for variations in motor speed by using pulse width modulation

Move the robot forwards and backwards, and turn left and right

# Descriptions
An Arduino Mega is the microcontroller for this system. It communicates with the Navigation system, sends signals to the motor drivers, and measures the speed.

The design for the robot's chassis started with a robotics kit purchased from amazon, but it was customized and turned into the towered, modular design that is present today.

The Motor Drivers for the robot are the Cytron MD20A, which is an H-Bridge that can control the polarity of power applied to the motor as well as the average voltage through PWM.

The driving DC gearmotors are from pololu. They come equipped with quadrature hall effect motor encoders that can be used to measure the speed and direction of the robot.

This README file constitutes a summary, for detailed design information and analysis of each component see signoff files in this repository. A seperate README exists for the software in the relevant sub-directory.
