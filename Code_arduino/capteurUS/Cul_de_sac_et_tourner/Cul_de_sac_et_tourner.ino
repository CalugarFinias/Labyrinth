// ajout bibliothèque du servo moteur
#include <Servo.h>. 

// Definition broches Trig et Echo pour ultrason
const int trigPin1 = 6;
const int echoPin1 = 7;
const int trigPin2 = 8;
const int echoPin2 = 9;
const unsigned long TempsMesure = 25000UL;
const float VitesseSon = 0.34; // vitesse son= 340 m/s

// Variables duree et distance
long duree1;
int distance1;
int distanceMm1;

long duree2;
int distance2;
int distanceMm2;

// objet servo moteur pour controler le servo
Servo myServo;

/*
 ******************************************************************************** 
*/
void setup() {
  pinMode(trigPin1, OUTPUT); // trigPin en Sortie 
  pinMode(echoPin1, INPUT); // echoPin en entrée
  pinMode(trigPin2, OUTPUT); // trigPin en Sortie 
  pinMode(echoPin2, INPUT); // echoPin en entrée
  Serial.begin(115200);
  myServo.attach(3); // pin du servo moteur
}
/*
 ******************************************************************************** 
*/
void loop()
{   
    myServo.write(0);
    delay(500);
    calculateDistance1();
    Serial.print(distance1);
    Serial.print(" \n");
    if(distance1<15)
    {
      calculateDistance2();
      Serial.print(distance2);
      Serial.print(" \n");
      if (distance2>10)
      {
        tournerADroite();
      }
      else
      {
        myServo.write(100);
        delay(500);
        calculateDistance1();
        Serial.print(distance1);
        Serial.print(" \n");
        if(distance1>10)
        {
          tournerAGauche();
        }
        else
        {
          demiTour();
        }
      }
    }
    delay(1000);
}
/*
 ******************************************************************************** 
*/
// Fonction de calcul de la distance mesurée par le capteur UltraSonic
int calculateDistance1()
{ 
   digitalWrite(trigPin1, LOW); 
   delayMicroseconds(2);
   // trigPin à HIGH state pour 10 micro secondes
   digitalWrite(trigPin1, HIGH); 
   delayMicroseconds(10);
   digitalWrite(trigPin1, LOW);
   duree1 = pulseIn(echoPin1, HIGH, TempsMesure); 
   // lit echoPin pour mesurer le parcours du son en micro secondes
   // 2: mesure aller +retour
   distanceMm1 = duree1*VitesseSon/2;
   distance1 = distanceMm1/100;
   return distance1;
}

int calculateDistance2()
{  
   digitalWrite(trigPin2, LOW); 
   delayMicroseconds(2);
   // trigPin à HIGH state pour 10 micro secondes
   digitalWrite(trigPin2, HIGH); 
   delayMicroseconds(10);
   digitalWrite(trigPin2, LOW);
   duree2 = pulseIn(echoPin2, HIGH, TempsMesure); 
   // lit echoPin pour mesurer le parcours du son en micro secondes
   // 2: mesure aller +retour
   distanceMm2= duree2*VitesseSon/2;
   distance2 = distanceMm2/100;
   return distance2;
}

void tournerADroite()
{
  Serial.print("je tourne à droite\n");
}

void tournerAGauche()
{
  Serial.print("je tourne à gauche\n");
}

void demiTour()
{
  Serial.print("je fais demi tour\n");
}
