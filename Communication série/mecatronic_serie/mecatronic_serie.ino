const int echoPin = 2; // Trigger Pin of Ultrasonic Sensor
const int trigPin = 3; // Echo Pin of Ultrasonic Sensor

long duration;
int distance;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  // Displays the distance on the Serial Monitor
  Serial.println(distance);
  delay(100);
  if(Serial.available()>0){
    Serial.println(distance);
    delay(100);  
  }
  
 /* if(Serial.available()>0){
    char fromPi = Serial.read();
    Serial.print("I received: ");
    Serial.println(fromPi);
    if(fromPi = 'E'){
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN,LOW);
      delay(1000); 
    }
  }*/
}
