## Moisture Probe MCU
* The code for the moisture probe scans between 5 varrying resistors to change the R1 value in a voltage divider
* An analog value is measured for each resistance and if it falls in an acceptable range that number is added to a rolling average
* This average is plugged into an equation to convert the resistance value into a moisture content
* The program sends this mositure content to the main microcontroller over serial communication
## Humidity MCU
* A humidity value is being constantly generate by the sensor and sent to the Arduino through a digital line
* The Raspberry Pi requests a value from the humidity microcontroller every time it takes a picture
* A sensor reading is then sent to the Pi over serial communication
## Temperature MCU
* A temperature value is being constantly generate by the sensor and sent to the Arduino through I2C communication
* The Raspberry Pi requests a value from the temperature microcontroller every time it takes a picture
* A sensor reading is then sent to the Pi over serial communication
