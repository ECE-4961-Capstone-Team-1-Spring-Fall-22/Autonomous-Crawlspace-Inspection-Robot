# Enviromental Sensing System


## Specs, Design, and Analysis:
This system was required to analyze data when triggered by the overall Raspberry Pi
It was also required to be modular and include a temperature sensor, humidity sensor, and wood moistrue probe

To match these rquirements, a system was developed where each sensor had its own MCU and returns data to the Raspberry Pi using SPI protocal
Each MCU will runs its respective sensor to collect a predetermined number of samples and then return the average to the Pi
A tag is inlcuded with the number so the Pi can differentiate between what was being sensed
This also allows future sensors to be easily added.

A wood moistrue probe was also included
This includes a two phase linear actuator design to raise the probe from 15 inches to 48 inches
Once in the wood, a resistance measurment is taken to detect MC%

Circuit Analysis as well as calculations were performed to verify each sysem

This README file constitutes a summary, for detailed design information and analysis of each component see signoff files in this repository
