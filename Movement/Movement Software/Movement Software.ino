const int M1channel1 = 18; //here we assign the encoder channels to their pin numbers
const int M1channel2 = 19;
const int M2channel1 = 20;
const int M2channel2 = 21;
const int M1PWM = 2; // the outputs to the drivers are linked to pin numbers
const int M1DIR = 17;
const int M2PWM = 3;
const int M2DIR = 16;
const int Encoder1Power = 15; //These pins power the encoders
const int Encoder2Power = 14;
char direct = 'S'; // This is the serial input from Raspberry Pi
volatile float M1C1freq = 0; //initalize the frequency from encoders
volatile float M1C2freq = 0;
volatile float M2C1freq = 0;
volatile float M2C2freq = 0;
float M1C1rpm;
float M1C2rpm;
float M2C1rpm;
float M2C2rpm;

void setup() {

 //setup the inputs to receive encoder data
pinMode(M1channel1, INPUT); 
pinMode(M1channel2, INPUT);
pinMode(M2channel1, INPUT);
pinMode(M2channel2, INPUT);

 //setup the outputs to the motor drivers
pinMode(M1PWM, OUTPUT);
pinMode(M1DIR, OUTPUT);
pinMode(M2PWM, OUTPUT);
pinMode(M2DIR, OUTPUT);

// Output Power to the Encoders
pinMode(Encoder1Power, OUTPUT);
pinMode(Encoder2Power, OUTPUT);
digitalWrite(Encoder1Power, HIGH);
digitalWrite(Encoder2Power, HIGH);

//setup the interrupts to detect the CPR of the motor encoders
//attachInterrupt(digitalPinToInterrupt(18), readM1Channel1, CHANGE);
//attachInterrupt(digitalPinToInterrupt(19), readM1Channel2, CHANGE);
//attachInterrupt(digitalPinToInterrupt(20), readM2Channel1, HIGH);
//attachInterrupt(digitalPinToInterrupt(21), readM2Channel2, CHANGE); 

//Open Serial Monitor
Serial.begin(9600);
}

void loop() { 

// That char variable is used to determine the direction of movement. 
if(Serial.available()){
        direct = Serial.read();
        delay(250);
}
// The next four If statements use the direct char from raspberry pi
// and change the direction of the motors accordingly
if (direct == 'F'){ //FORWARD
  digitalWrite(M1DIR, HIGH);
  digitalWrite(M2DIR, HIGH);
  analogWrite(M1PWM, 175);
  analogWrite(M2PWM, 175);
}
delay(20);
if (direct =='B'){ //BACKWARD
  digitalWrite(M1DIR, LOW);
  digitalWrite(M2DIR, LOW);
  analogWrite(M1PWM, 175);
  analogWrite(M2PWM, 175);
}
delay(20);
if (direct =='L'){ //LEFT
  digitalWrite(M1DIR, HIGH);
  digitalWrite(M2DIR, LOW);
  analogWrite(M1PWM, 100);  
  analogWrite(M2PWM, 100);
}
delay(20);
if (direct =='R'){ //RIGHT
  digitalWrite(M1DIR, LOW);
  digitalWrite(M2DIR, HIGH);
  analogWrite(M1PWM, 100);
  analogWrite(M2PWM, 100);
}

delay(20);
if (direct =='S'){ //STOP  
  analogWrite(M1PWM, 0);
  analogWrite(M2PWM, 0);
}

// Convert Pulse Frequencies to Speeds
M1C1rpm = M1C1freq * 1.27 / 12;
//float M1C2rpm = M1C2freq / 12;
M2C1rpm = M2C1freq * 1.27  / 12;
//float M2C2rpm = M2C2freq / 12;

//Output Speeds to Pi
delay(250);
Serial.println(M1C1rpm);
//Serial.println(M1C2rpm);
Serial.println(M2C1rpm);
//Serial.println(M2C2rpm);

attachInterrupt(digitalPinToInterrupt(18), readM1Channel1, HIGH);
//attachInterrupt(digitalPinToInterrupt(19), readM1Channel2, HIGH);
attachInterrupt(digitalPinToInterrupt(20), readM2Channel1, HIGH);
//attachInterrupt(digitalPinToInterrupt(21), readM2Channel2, HIGH);
}

//Now I need to read the Encoder channels with those ISRs
//I'm also calculating the frequency of the pulses in here
void readM1Channel1(){
if(direct != 'S'){
  float M1C1high = pulseIn(M1channel1,HIGH);
  float M1C1low = pulseIn(M1channel1,LOW);
  M1C1freq = 1000000 / (M1C1high + M1C1low);
  detachInterrupt(digitalPinToInterrupt(18));
  }
  else 
  M1C1freq = 0;
  detachInterrupt(digitalPinToInterrupt(18));
}

/*void readM1Channel2(){
if(direct != 'S'){
  float M1C2high = pulseIn(M1channel2,HIGH);
  float M1C2low = pulseIn(M1channel2,LOW);
  M1C2freq = 1000000 / (M1C2high + M1C2low);
  detachInterrupt(digitalPinToInterrupt(19));
  }
  else 
  M1C2freq = 0;
  detachInterrupt(digitalPinToInterrupt(19));
}*/

void readM2Channel1(){
  if(direct != 'S'){
  float M2C1high = pulseIn(M2channel1,HIGH);
  float M2C1low = pulseIn(M2channel1,LOW);
  M2C1freq = 1000000 / (M2C1high + M2C1low);
  detachInterrupt(digitalPinToInterrupt(20));
  }
  else 
  M2C1freq = 0;
  detachInterrupt(digitalPinToInterrupt(20));
}

/*void readM2Channel2(){
if(direct != 'S'){
  float M2C2high = pulseIn(M2channel2,HIGH);
  float M2C2low = pulseIn(M2channel2,LOW);
  M2C2freq = 1000000 / (M2C2high + M2C2low);
  detachInterrupt(digitalPinToInterrupt(21));
  }
  else 
  M2C2freq = 0;
  detachInterrupt(digitalPinToInterrupt(21));
}*/
