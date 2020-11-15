const int echoPinLeft = 2; // Trigger Pin of Left Ultrasonic Sensor
const int trigPinLeft = 3; // Echo Pin of Left Ultrasonic Sensor
const int echoPinRight = 4; // Trigger Pin of Right Ultrasonic Sensor
const int trigPinRight = 5; // Echo Pin of Right Ultrasonic Sensor

String new_inner_command ="";

String left_to_pi;
String right_to_pi;
String data_to_pi;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(trigPinLeft, OUTPUT);
  pinMode(echoPinLeft, INPUT);
  pinMode(trigPinRight, OUTPUT);
  pinMode(echoPinRight, INPUT);
}

void loop() {
  left_to_pi = readLeftCaptor();
  right_to_pi = readRightCaptor();
  data_to_pi = left_to_pi + right_to_pi;
  Serial.println(data_to_pi);
  delay(200);
  new_inner_command = get_serial_command_from_pi();
  messageDecode(new_inner_command);
  
}

String readLeftCaptor() {
  long duration;
  int distance_left;
  String left="left ";
  String space = " "; 
  
  digitalWrite(trigPinLeft, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPinLeft, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPinLeft, LOW);
  duration = pulseIn(echoPinLeft, HIGH);
  distance_left = duration * 0.034 / 2; 
  left = left + String(distance_left);
  left = left + space;
  return left;
}

String readRightCaptor() {
  long duration;
  int distance_right;
  String right = "right ";
  
  digitalWrite(trigPinRight, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPinRight, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPinRight, LOW);
  duration = pulseIn(echoPinRight, HIGH);
  distance_right = duration * 0.034 / 2; 
  right = right + String(distance_right);
  return right;
}

String get_serial_command_from_pi(){
  String inner_message ;
  if(Serial.available()>0){
    while(Serial.available()>0){
      char in_char = Serial.read();
      inner_message +=in_char;
      delay(2);
      }
    }
  return inner_message;
}

void messageDecode(String command){
  if (command == "a"){
    digitalWrite(LED_BUILTIN, HIGH);
  }
  else {
    digitalWrite(LED_BUILTIN, LOW);
  }
}
