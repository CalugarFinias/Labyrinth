#define DISTANCE_ERROR 5  // marge à partir de laquel on accepte la mesure ou pas
#define US_SENSOR_TRIG_PIN 2
#define US_SENSOR_ECHO_PIN 3

struct USsensor{
  unsigned char triggerPin;
  unsigned char echoPin;
  double lastDistance;
}usSensor;

double distanceUSsensor;

void setup() {
  Serial.begin(9600);
  
  usSensorInitialize(&usSensor, US_SENSOR_TRIG_PIN, US_SENSOR_ECHO_PIN); 
  distanceUSsensor = 0;
}
 
void loop() { 
  Serial.println(distanceComputation(usSensor)); 
}

void usSensorInitialize(USsensor *usSensor, unsigned char trig, unsigned char echo){
  usSensor->triggerPin = trig;
  usSensor->echoPin = echo;
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
}

double distanceComputation(USsensor *usSensor){
  double pulseDuration, distanceInCM;

  digitalWrite(usSensor->triggerPin, HIGH);
  delayMicroseconds(10);                   
  digitalWrite(usSensor->triggerPin, LOW);

  pulseDuration = pulseIn(usSensor->echoPin, HIGH);  // retourne des micro secondes
  
  // Pour le numérateur, on prend la durée que met l'ultrason pour être détecté /2 (allé + retour = 2x la distance voulue)
  //      et on multiplie par 340 qui est la vitesse du son en m/s afin d'obtenir la distance en m.
  // Ensuite on utilise "pow(nombre, exposant)" pour transformer en cm la distance en donné en m.
  distanceInCM = (pulseDuration*340/2)/pow(10,4);  

  // Test permettant de vérifier si la mesure prise est correcte ou pas (si elle est pas trop différente de la précédente).
  //    - La première comparaison permet de vérifier si la valeur actuel n'est pas trop différente de la
  //      précédente (ici 5x, à choisir) car il y a peu de chance que le robot passe de 40cm à 200cm en 1s.
  //    - La deuxième comparaison permet de s'assurer de ne pas prendre en compte la variable inisialisé (=0).
  //    - La troisième s'assure qu'on est pas dans des distances trop courte car 5x 2cm = 10cm => ce qui n'est pas 
  //      impossible que le robot fasse comme distance vu la courte distance.
  /*
  if((distanceInCM > DISTANCE_ERROR*usSensor->lastDistance) && (usSensor->lastDistance != 0) && (usSensor->lastDistance > 10.0))
    distanceInCM = usSensor->lastDistance;

  usSensor->lastDistance = distanceInCM;*/
  return distanceInCM;
}
