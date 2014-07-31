int fsrPin = 0;
boolean sendOnce = true;

void setup() {
  Serial.begin(9600);
}

void loop() {
  
  int strength = analogRead(fsrPin);
  
  if(strength > 500 && sendOnce) {
     Serial.println("MESSAGE");
     sendOnce = false;
  }
  
  delay(500);
}

