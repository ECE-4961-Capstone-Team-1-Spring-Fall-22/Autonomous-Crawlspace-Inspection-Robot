# Croomba Experimental Data
## System Testing

## Power
### Main Power LN 2 & 5
Trial Number (N)|Current(A) | Voltage (V)  |
|:---: | :---:|:----:|
| 1 |       A |        V|
| 2 |       A |        V|
| 3 |       A |        V|

### Navigation LN 7A & 8A
Trial Number (N)|Current(A) | Voltage (V)  |
|:---: | :---:|:----:|
| 1 |       A |        V|
| 2 |       A |        V|
| 3 |       A |        V|
### Network Router LN 9A & 10A
Trial Number (N)|Current(A) | Voltage (V)  | 
|:---: | :---:|:----:|
| 1 |       A |        V|
| 2 |       A |        V|
| 3 |       A |        V|
### Movement LN 11A & 12A
Trial Number (N)|Current(A) | Voltage (V)  | 
|:---: | :---:|:----:|
| 1 |       A |        V|
| 2 |       A |        V|
| 3 |       A |        V|

### Environmental Sensing  LN 13A & 14A
Trial Number (N)|Current(A) | Voltage (V)  | 
|:---: | :---:|:----:|
| 1 |       A |        V|
| 2 |       A |        V|
| 3 |       A |        V|
## Navigation


## Enviromental Sensing
### Temperature
The sensor was placed outside at different times and compared to the ambient temperature given by Weather.com. The test was preformed like this because the commercially available sensor turned out to be incredibly slow and inaccurate. It was also done in this way because an outdoor enviroment is where the robot will be used. 
| Date/Time Recorded | System Temperature Sensor (°F) | Website Listed Temperature (°F) | Percent Error (%) | Difference (°F) |
| :----------------: | :----------------------------: | :-----------------------------: | :---------------: | :-------------: |
| 11/5/2022 23:30    | 62.825                         | 63                              | 0.28              | 0.175           |
| 11/6/2022 0:44     | 61.5375                        | 61                              | 0.88              | 0.5375          |
| 11/6/2022 1:23     | 57.925                         | 59                              | 1.82              | 1.075           |
| 11/6/2022 11:53    | 62.2375                        | 64                              | 2.75              | 1.7625          |
| 11/6/2022 15:06    | 71.125                         | 70                              | 1.61              | 1.125           |
| 11/6/2022 16:33    | 66.6875                        | 67                              | 0.47              | 0.3125          |
| 11/6/2022 21:46    | 66.5375                        | 64                              | 3.96              | 2.5375          |

The table shows that the system temperature sensor has exceptional accuarcy when compared to a purchased sensor. MORE ABOUT MAX ERROR AFTER LAST DATA POINT IS IN
### Humidity
The sensor was placed outside at different times and compared to the  humidity given by Weather.com. The test was preformed like this because the commercially available sensor turned out to be incredibly slow and inaccurate. It was also done in this way because an outdoor enviroment is where the robot will be used. 
| Date/Time Recorded | System Humidity Sensor (%RH) | Website Listed Humidtiy (%RH) | Percent Error (%) | Difference (%RH) |
| :----------------: | :--------------------------: | :---------------------------: | :---------------: | :--------------: |
| 11/5/2022 23:30    | 82.3                         | 84                            | 2.02              | 1.7              |
| 11/6/2022 0:44     | 87.1                         | 89                            | 2.13              | 1.9              |
| 11/6/2022 1:23     | 93.1                         | 95                            | 2.00              | 1.9              |
| 11/6/2022 11:53    | 86.9                         | 86                            | 1.05              | 0.9              |
| 11/6/2022 15:06    | 83.2                         | 84                            | 0.95              | 0.8              |
| 11/6/2022 16:33    | 95.4                         | 99                            | 3.64              | 3.6              |
| 11/6/2022 21:46    | 92.8                         | 96                            | 3.33              | 3.2              |

The table shows that the humidity sensor is well within out desired range for accuracy. The datasheet for the DHT22 sensor says the accuracy should be ±2 %RH. While this experiment found several points outside this range, it seems to mainly be at the higher humidity values where the accuracy decreases. However, even at these points the accuracy is at a very acceptable level.   MORE ABOUT MAX ERROR AFTER LAST DATA POINT IS IN

### Moisture Content
The Moisture Probe was first tested using axial resistors so that a known value could be tested. The resistors were also checked on a multimeter so that the true value could be compared along with the listed value. This test provided limited results due to the availablity of resistors to test. However, it is secondary to the full moisture content testing and was mostly used for troubleshooting.
| Known Resistance (MΩ) | Multimeter Result (MΩ) | Probe Result (MΩ) |
|       :---:           |       :----:           |    :----:         |
| 1                     | 1.02                   | 1.02              |
| 2.2                   | 2.23                   | 2.23              |
| 4.7                   | 4.83                   | 4.82              |
| 10                    | 9.88                   | 9.78              |
| 47                    | 51.0                   | 46.0              |

The results above were all found to be accurate within 1% error except for the 47 MΩ test which had about 10% error. This is because it was found that the first two stages had greatly increased accuracy compared to the stages with larger resistors used in the voltage divider. After much research, it was found that Arduino analog read pins prefer a smaller input impedance which was unknown at the time of designing. This could be fixed in future revisions by switching out the microcontroller used. 


The system was used on blocks of wood with differing moisture contents and compared to the results given by a commercial wood moisture probe. Forcing a piece of wood to be a certain moisture content caused some problems with this experimentation. Leaving the wood pieces in a steamy room  allowed values between 7% and 11% to be tested but the higher values could not be achieved this way.  Instead, a piece of wood was soaked with water and tested at different times as the wood dried out and its moistrue content fell. This allowed the higher values to be tested.
| COTS Moisture Content Probe | System Moisture Content Probe | 
| :---:                       |    :----:                     | 
| 7                           | 6.86                          |
| 9                           | 7.34                          |
| 10                          | 8.13                          |
| 10                          | 8.31                          |
| 11                          | 9.51                          |
| 13                          | 11.31                         |
| 13                          | 14.44                         |
| 14                          | 15.89                         |
| 15                          | 12.26                         |
| 16                          | 17.55                         |
| 17                          | 16.87                         |
| 19                          | 18.55                         |
| 24                          | 22.4                          |
| 25                          | 23.26                         |
| 26                          | 23.54                         |

As can be seen from the table above, the actual moisture content value is not 100% accurate to the commercial probe. However, all values fall within ±3 of the expected percentage value. The collected data shows that the system is detecting changes within the moisture content of plank. Based on the raw resistance values which were seen in the previous section. It is believe some of this error comes from the equation created to convert resistance to wood mositure percentage. 

## Movement
### The Height Constraint
For the first test we measured the height of the robot with a tape measure. This was done in order to ensure that the 16 inch height constraint was met. This experiment was conducted twice and the results are displayed below. 
| Trial Number | Height of Robot |
|:---:         | :---:           |
| 1            | 15.1875 inches  |
| 2            | 15.1875 inches  |

The above results show that the robot is 15.1875 inches tall. That number is less than 16 inches, and thus the height constraint has been met
### Drive Motor Rotational Speed
The purpose of this test is to confirm the robot is moving as fast as it thinks that it is. In this test the robot’s internal measurement of the movement speed within the program was analyzed to determine its validity. Those values were compared against a measurement obtained by using a digital tachometer placed into contact with the drive wheel. The values in the table below are in units of RPMs.
|Robot's Reading|Tachometer Reading|
|:---:          |:---:             |
|219.7          |220               |
|218.5          |219.2             |
|220.1          |219.8             |
|219.2          |219.9             |
|220            |220.6             |

These results show that the Autonomous Crawl Space Inspection Robot is correctly measuring its movement speed. 
### Linear Speed
For this experiment the team wanted to measure the robot’s linear speed. To do this, we measured out 10 feet with a tape measure, and then used a stopwatch to determine how quickly the robot covered that distance. The desired speed is 1 foot per second. The units in the table below are in seconds and feet per second respectively.
|Travel Time|Speed|
|:---:      |:---:|
|5.56       |1.8  |
|Travel Time|Speed|
|Travel Time|Speed|
|Travel Time|Speed|
|Travel Time|Speed|

These results show that the robot is moving faster than expected. To accomodate for this, the maximum PWM value will need to be lowered.
