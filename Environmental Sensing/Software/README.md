# Software Writeup

## What the code does
This file contains 4 programs that make up the environmental sensing system's software.
* The Temp Arduino file handles receiving data from the temperature sensor over I2C and sending that data to the main MCU using serial communication.
* The Humidity Arduino file handles receiving data from the temperature sensor over a single digital wire and sending that data to the main MCU using serial communication.
* The MC Arduino file handles the moisture content measurement. This code flips through 5 digital outputs to control the values of R1 in the voltage divider circuit. It takes resistance measurements at each point and averages the acceptable measurements before converting from Ohms to %MC.
* The Stitching python file handles the image stitching. The files are automatically sorted into an array and have their MC values overlaid on the image. The images are then stitched together by manually choosing which pictures were taken consecutively.
- This code also handles reading the temperature and humidity values from a text file, averaging the values, and displaying any values which are outside the acceptable range of 2 standard deviations.

## Dependencies
* Adafruit DHT Library (Arduino Internal)- Used to pull data from the humidity sensor over a single-wire data line. 
* Adafruit MCP9808 Library (Arduino Internal) - Used to pull data from the temperature sensor over I2C protocol. 
* https://github.com/KEDIARAHUL135/PanoramaStitchingP2 - Provided basic algorithm for stitching 2 images together and pulling images into an array.

# Code Instructions
For all Arduino codes, the instructions are the same.
1. Build a circuit using Arduino Nano based on the schematic found [here](https://github.com/ECE-4961-Capstone-Team-1-Spring-Fall-22/Autonomous-Crawlspace-Inspection-Robot/blob/main/Environmental%20Sensing/Environmental%20Sensing%20Schematic.pdf)
2. Pull the Arduino file and place it in a folder with the same name as the code.
3. Download all relevant libraries by going into the "Sketch" menu, choosing "Include Library" and then importing the correct library from Arduinos internal system.
4. Set up the serial port by going into the "Tools" menus and choosing the correct device.
5. Upload code to the board.

The image stitching code instructions are as follows
1. Ensure that OpenCV and python are both downloaded and can successfully compile.
2. Places pictures in the folder called "TestPics" and ensure the folder is in the same directory as the program.
3. Ensure pictures are numbered 0 to max in order of taking.
4. Ensure the stitching lines in the code are set to match the pictures which you want to be stitched.
5. Run code, results will be shown in the plot initially but will be saved upon closing the plot.
* NOTE1: There are additional algorithms commented out that can be seen in this code. Each one was found the work for some cases and not for others.
* NOTE2: While this algorithm works for a straight view of an object, it was found in the late stages of development that perspective changes will cause issues. This is the topic of much research at the moment and further algorithm development will be necessary.
