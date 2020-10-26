//============================================ IO Pins ============================================
// Pins used on Arduino Uno

#include "TimerOne.h"
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"


 
#define rEncoder 2
#define lEncoder 3

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
Adafruit_DCMotor *myMotorG = AFMS.getMotor(2);
Adafruit_DCMotor *myMotorD = AFMS.getMotor(1);



//======================================== Global Variables =======================================

// Variables used in interrupts
volatile unsigned long rightWheel;
volatile unsigned long leftWheel;

unsigned long previousMillis=0;
int interval =100;
// PID Values
double inputG=0,inputD=0, LastErrorRot=0,LastErrorLin=0, proportionalRot=0,proportionalLin=0, derivativeRot=0,derivativeLin=0, integralRot=0,integralLin=0;



double outputsPid[2];
// pidcount is used to divide the total error (integral formula)
int pidcountRot = 1;
int pidcountLin =1;

// PID Multipliers
double kpRot = 0; // 0.1
double kiRot = 0; 
double kdRot = 0; 

double kpLin = 0; // 0.6
double kiLin = 0; //entre 0.2 et 0.6 ?
double kdLin = 0;  


//============================================= Setup =============================================
void setup(){
 
  Serial.begin(9600);
   AFMS.begin();
  pinMode(rEncoder, INPUT);
  pinMode(lEncoder, INPUT);
  
 
  // Enable the pull up resistors for the encoders
  digitalWrite(rEncoder, HIGH);
  digitalWrite(lEncoder, HIGH);
  //Enable interrupts 0 and 1 on pins D2 and D3
  attachInterrupt(0, rightEncoderISR, RISING);
  attachInterrupt(1, leftEncoderISR, RISING);
 


}// End Setup

//============================================= Loop ==============================================
void loop(){
unsigned long currentMillis=millis();
if ( currentMillis-previousMillis>= interval){ // appel de fonction toutes les 100 ms
    previousMillis=currentMillis;
    calculPid(0,500); // calculPid( setPointRotation [rad/s] , setPointLineaire [mm/s] )
 /*  Serial.println("ROTATIONEL : ");
  Serial.println(outputsPid[0]);
  Serial.println("LINEAIRE : ");
  Serial.println(outputsPid[1]);*/

   double somPid= (outputsPid[0]+outputsPid[1] ); // Rot+Lin  => M1=Droite
   double diffPid= (outputsPid[1]-outputsPid[0]); // Lin -Rot => M2=Gauche


/*
  if(somPid<0){
      myMotorD->setSpeed(abs(somPid));// set speed of motor (0-255)
 myMotorD->run(BACKWARD);
   Serial.println("PWM D:  ");
  Serial.println(somPid);
  
    }
  else {
    myMotorD->setSpeed(somPid);// set speed of motor (0-255)
  myMotorD->run(FORWARD);
   Serial.println("PWM D:  ");
  Serial.println(somPid);
  }
 if(diffPid<0){
   myMotorG->setSpeed(abs(diffPid));// set speed of motor (0-255)
  myMotorG->run(BACKWARD);
  Serial.println("PWM G:  ");
  Serial.println(diffPid);
  }
 else{
  myMotorG->setSpeed(diffPid);// set speed of motor (0-255)
  myMotorG->run(FORWARD);
  Serial.println("PWM G:  ");
  Serial.println(diffPid);
  } */

 myMotorG->setSpeed(140);// set speed of motor (0-255)
  myMotorG->run(FORWARD);
 
 myMotorD->setSpeed(140);// set speed of motor (0-255)
  myMotorD->run(FORWARD);
  }



}

void calculPid(double setPointRot, double setPointLin){
  
  inputG = leftWheel;
  double vitG= ((inputG*10*20.7)/20); //inputG = le nombre de ticks pour 0.1s  et vitG la vitesse en tr/s car *10 pour 1sec et /20 pr 1tr et *20.7 pour passer de tr/s à mm/s
/*Serial.println("TICKS G ");
  Serial.println(inputG);*/
Serial.println("VIT MESURE G");
 Serial.println(vitG); 
  inputD= rightWheel;
  double vitD= ((inputD*10*20.7)/20); // vit en mm/s
/* Serial.println("TICKS D ");
  Serial.println(inputD);*/
Serial.println("VIT MESURE D");
  Serial.println(vitD);
  
  leftWheel = 0;
  rightWheel=0;
  

double mesureVitRot= (vitD-vitG)/150;// 15cm= D roue
double mesureVitLin= (vitD+vitG)/2;

/* Serial.println("LAST EROR Rot");""
  Serial.println(LastErrorRot); */
  // Calculate the PID values Rotation
  proportionalRot = setPointRot - mesureVitRot; //Erreur vit desire et vit reele
/*Serial.println("ERROR ROT :  ");
Serial.println(proportionalRot); */
  derivativeRot = proportionalRot - LastErrorRot;
  integralRot = (integralRot + proportionalRot)/pidcountRot; 
/* Serial.println("INTEGRAL ROT :  ");
Serial.println(integralRot); */
  // Scale the PID values and save total as output
  outputsPid[0] = kpRot * proportionalRot + kdRot * derivativeRot + kiRot * integralRot;
  outputsPid[0]= outputsPid[0]*(150/2);
  
  // Save variables for next time
  LastErrorRot = proportionalRot;
  pidcountRot++;

///////////////////////////////////////////////////////////////////////////////////////////////
   // Calculate the PID values Linear
  proportionalLin = setPointLin- mesureVitLin;//Erreur vit desire et vit reele
  derivativeLin = proportionalLin - LastErrorLin;
  integralLin = (integralLin + proportionalLin/pidcountLin);
  Serial.println("INTEGRAL LIN :  ");
Serial.println(integralLin); 
  /*Serial.println("ERROR LIN :  ");
  Serial.println(proportionalLin); */
  // Scale the PID values and save total as output
  outputsPid[1] = kpLin * proportionalLin + kdLin * derivativeLin + kiLin * integralLin;
  
  // Save variables for next time
 /* Serial.println("LAST EROR Lin ");
  Serial.println(LastErrorLin); */
  LastErrorLin = proportionalLin;
  pidcountLin++;

  
}


//========================================== Encoder ISRs =========================================
// Interrupts
void rightEncoderISR(){
  rightWheel++;
 
}

void leftEncoderISR(){
  leftWheel++;
}

//=================================================================================================
