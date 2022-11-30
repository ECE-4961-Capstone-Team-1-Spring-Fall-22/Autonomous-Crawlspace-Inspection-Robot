int trigPin = 11; //trigger 
int lastTrig = 0;
int trigState = 0;

void setup() {
  pinMode(trigPin, INPUT); //Setup trigger pin
  //Setup analog pins as digital
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);
  pinMode(A3, OUTPUT);
  pinMode(A4, OUTPUT);
  pinMode(A5, INPUT);
  digitalWrite(A0, HIGH);
  digitalWrite(A1, HIGH);
  digitalWrite(A2, HIGH);
  digitalWrite(A3, HIGH);
  digitalWrite(A4, HIGH);

  pinMode(12, OUTPUT);
  digitalWrite(12, HIGH);

  Serial.begin(9600);
  delay(10);
}

void loop() {
  //Code for test run
  while(1) {
    Serial.print(random(7, 25));
    delay(5);
  }

  //serial.println("Starting--------------------------------------------");
  float testVal = 0;
  //testVal = testMC();
  testVal = testMC();
  float MCVal = 21.844*pow(testVal, -.12);
  int MCVal_int = int(MCVal);
  //serial.println(testVal);
  Serial.println(MCVal);
  delay(2000);
}

float testMC() {
  int probeVal;
  int counter = 0;
  float newMC;
  float avgMC = 0;
  int avgCount = 0;
  
  for(int i=1; i <= 5; i++) { 
    setPin(i);
    delay(5000);
    probeVal = analogRead(A5);
    delay(50);
    if(probeVal > 400 && probeVal < 1000) {
      //serial.print("probe: "); //serial.println(probeVal);
      newMC = specificVal(probeVal, i);
      avgMC = ((avgMC*avgCount)+newMC)/(avgCount+1);
      avgCount++;
      delay(50);
    }
    else {
      //serial.print(i); //serial.print(" value ");//serial.println(probeVal);
      counter++;
    }
  }

// int i = 5;
//  setPin(i);
//  probeVal = analogRead(A5);
//  delay(50);
//  MC = specificVal(probeVal, i);
  if(counter == 5) avgMC = 0;
  return avgMC;
}

float specificVal(int pVal, int iteration) {
  float R1;
  float R2;
  float Vin = 5;
  float V2;
  switch(iteration) {
    case 1:
      R1 = 0.82;
      //serial.println(R1);
      delay(20);
      break;
    case 2:
      R1 = 4.7;
      //serial.println(R1);
      delay(20);
      break;
    case 3:
      R1 = 47;
      //serial.println(R1);
      delay(20);
      break;
    case 4:
      R1 = 470;
      //serial.println(R1);
      delay(20);
      break;
    case 5:
      R1 = 10000;
      //serial.println(R1);
      delay(20);
      break; 
  }
  V2 = pVal * 0.00488;
  //serial.print("V2 ");//serial.println(V2);
  delay(20);
  R2 = R1/((Vin/V2)-1);
  //serial.print("R2 ");//serial.println(R2);
  delay(20);
  return R2;
}

//sets port C and PRE_SHIFTS integer for next set
void setPin(int iteration) {
  switch(iteration) {
    case 1:
      //serial.println("set 1------------------------------------");
      digitalWrite(A0, LOW);
      digitalWrite(A1, HIGH);
      digitalWrite(A2, HIGH);
      digitalWrite(A3, HIGH);
      digitalWrite(A4, HIGH);
      delay(20);
      break;
    case 2:
      //serial.println("set 2------------------------------------");
      digitalWrite(A0, HIGH);
      digitalWrite(A1, LOW);
      digitalWrite(A2, HIGH);
      digitalWrite(A3, HIGH);
      digitalWrite(A4, HIGH);
      delay(20);
      break;
    case 3:
      //serial.println("set 3------------------------------------");
      digitalWrite(A0, HIGH);
      digitalWrite(A1, HIGH);
      digitalWrite(A2, LOW);
      digitalWrite(A3, HIGH);
      digitalWrite(A4, HIGH);
      delay(20);
      break;
    case 4:
      //serial.println("set 4------------------------------------");
      digitalWrite(A0, HIGH);
      digitalWrite(A1, HIGH);
      digitalWrite(A2, HIGH);
      digitalWrite(A3, LOW);
      digitalWrite(A4, HIGH);     
      delay(20);
      break;
    case 5:
      //serial.println("set 5------------------------------------");
      digitalWrite(A0, HIGH);
      digitalWrite(A1, HIGH);
      digitalWrite(A2, HIGH);
      digitalWrite(A3, HIGH);
      digitalWrite(A4, LOW);  
      delay(20);
      break;
    
  }

}
