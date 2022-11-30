# Mechanical Movement Software ReadMe
## What the Software Does
This Arduino Program accepts a serial input that is used to change the direction of the drive motors. 
This program uses Interrupts to measure the frequency of the Motor Encoder Signals.
Those Motor Encoder Signals are then converted to RPMs and Output to Serial.

## Dependencies
This program calls upon no additional libraries or other files.
Some form of serial input to the program is required for motor direction change.

## How to Install
This Program can be Uploaded to an Arduino Mega by using the Arduino IDE.
First, connect a USB cable between your computer and the Arduino Mega.
Second, in the IDE, under Tools, ensure that the board is set to "Arduino Mega or Mega 2560" the processor is the ATmega2560.
Third, ensure that the correct COM port has been selected.
Finally, in the IDE, click upload

## How to Run
The Program will immediately start outputting the speed, and it can be seen in the serial monitor.
The speed will consistently be 0 unless the interrupts are pinging.
