# Croomba Experimental Data
## System Testing

## Power
### Main Power LN 2 & 5
Trial Number (N)|Current(A) | Voltage (V)  |
|:---: | :---:|:----:|
| 1 |       0.526 A |        13.26 V|
| 2 |       0.627 A |        13.26 V|
| 3 |       0.675 A |        12.85 V|
| 4 |       1.265 A |        12.68 V|
| 5 |       1.326 A |        12.75 V|

### Navigation LN 7A & 8A
Trial Number (N)|Current(A) | Voltage (V)  |
|:---: | :---:|:----:|
| 1 |       0.7 A |    5.33 V|
| 2 |      0.6 A |       5.34 V|
| 3 |      0.79 A |       5.33 V|
| 4 |       0.7 A |        12.68 V|
| 5 |       1.326 A |        12.75 V|

### Network Router LN 9A & 10A
Trial Number (N)|Current(A) | Voltage (V)  | 
|:---: | :---:|:----:|
| 1 |      0.1 A |       5.3 V|
| 2 |      0.12 A |       5.32 V|
| 3 |       0.12 A |       5.31 V|
| 4 |       0.28 A |        5.31 V|
| 5 |       0.33 A |        5.3 V|

### Movement LN 11A & 12A
Trial Number (N)|Current(A) | Voltage (V)  | 
|:---: | :---:|:----:|
| 1 |       0.526 A |        13.26 V|
| 2 |       0.627 A |        13.26 V|
| 3 |       0.675 A |        12.85 V|
| 4 |       1.265 A |        12.68 V|
| 5 |       1.326 A |        12.75 V|

### Environmental Sensing  LN 13A & 14A
Trial Number (N)|Current(A) | Voltage (V)  | 
|:---: | :---:|:----:|
| 1 |      0.0642 A |       5.24 V|
| 2 |       0.0645 A |       5.23 V|
| 3 |       0.0644 AA |       5.26 V|
| 4 |       0.0.065 A |        5.31 V|
| 5 |       0.064 A |        5.3 V|

###




## Navigation


## Enviromental Sensing
### Temperature
The sensor was placed outside at different times and compared to the ambient temperature given by Weather.com. The test was preformed like this because the commercially available sensor turned out to be incredibly slow and inaccurate. It was also done in this way because an outdoor enviroment is where the robot will be used. 
| System Temperature Sensor | Website Listed Temperature | 
|          :---:            |            :----:          |
| 62.82                     | 63                         |
| 61.58                     | 61                         |
### Humidity
The sensor was placed outside at different times and compared to the  humidity given by Weather.com. The test was preformed like this because the commercially available sensor turned out to be incredibly slow and inaccurate. It was also done in this way because an outdoor enviroment is where the robot will be used. 
| System Humidity Sensor | Website Listed Humidtiy | 
|         :---:          |          :----:         |
| 82.25                  | 84                      |
| 87.10                  | 89                      |

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


The system was used on blocks of wood with differing moisture contents and compared to the results given by a commercial wood moisture probe.
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
