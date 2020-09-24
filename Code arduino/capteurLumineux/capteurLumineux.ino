#define LIGHT_SENSOR_PIN 4
#define LOOP_WAIT 1 // nombre de seconde à attendre entre chaque prise de mesure 

struct lightSensor{
  unsigned char detectionPin;
  bool lineIsDetected;  // 0 détecte rien / 1 détecte qlq chose  
}lightSensor1;


void setup() {
  Serial.begin(9600);

  lightSensorInitialize(&lightSensor1, LIGHT_SENSOR_PIN);
}
 
void loop() {  
  delay(LOOP_WAIT*1000);

  //Serial.println();
}

void lightSensorInitialize(lightSensor *lightSensor1, unsigned char detectionPin){
  lightSensor1->detectionPin = detectionPin;
  lightSensor1->lineIsDetected = 0;
  pinMode(detectionPin, OUTPUT);
}
