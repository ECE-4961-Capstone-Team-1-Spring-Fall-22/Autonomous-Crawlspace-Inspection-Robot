# Mechanical Movement System
The mechanical movement subsystem is essential for the operation 
of the Autonomous Crawlspace Inpsection Robot. The main purpose
of this system is to provide the robot with the ability to move.

# Specs, Design, and Analysis: 
This subsystem has several specifications that need to be met. 

Firstly, the robot must be able to "roomba around." This 
specification on its own is not enough to fuel a design because 
it is not a quantitative or measurable criteria. In order to
solve this issue, the phrase "roomba around" must be more 
accurately defined. The robot needs to move at approximately 
0.3 meters per second. This speed is fast enough to obtain 
quality measurements and adhere to the sensors' sampling rates, 
but slow enough so that the robot does not outrun the operators 
that would oversee it.The robot should also be able to cover a 
25 square foot area in under an hour. This confirms that the 
robot will have enough battery power to sustain longer operating 
times. In short the robot needs to move at 0.3 m/s

Next up is load. As the structual foundation of the robot the main 
chassis must be able to support all the components that will be on 
the robot. Therefore the weight of the robot is important because 
it has a direct effect on how much torque the motors need to output 
in order to meet the velocity specifcation, and it also affects the 
strength of material that the robot can be made out of as well as 
how the robot is constructed as the robot must be able to support 
its own weight. Therefore, a weight limit of 10kg has been placed 
on the robot.

Together the robot's weight and speed specs serve as the parameters 
for a motor analysis. The 2 drive motors must be able to generate 
enough rpm to achieve 0.3 m/s, but also have the torque output 
necessary to move a robot that weighs up to 10 kg. 

A robotics kit that contained a chassis strong enough to support the 
load and motors strong enough the move the robot at the desired speed 
was identified and selected. This robotics kit serves as the structual 
and mechanical foundation for the project. The motors also come 
equipped with Hall sensors that can be used to detect errors in the
robot's movement. 

The Movement system must be able to communicate with the navigation 
system in order to receive its directional input. The inclusion of a 
microcontroller in the design satisfies that requirement, but also 
allows for new possibilities. With a microcontroller, motor speed can 
be set by using pulse width modulation, and the motors can be 
monitored to ensure that they are operating properly. The Arduino 
Nano Every was chosen because it has 16 digital GPIO pins and 5 of
them can be used for PWM. 

Those PWM pins have the capability to directly control the motors speed 
when interfaced with a motor driver. The L298N motor driver accepts input
from the Arduino and amplifies the signals so that the motor can receive them.
