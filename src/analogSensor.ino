#include "SharpIR.h"

#define model 1080

#define IRP1 A0
#define IRP2 A1
#define IRP3 A2

SharpIR sensor1 = SharpIR(IRP1, model);
SharpIR sensor2 = SharpIR(IRP2, model);
SharpIR sensor3 = SharpIR(IRP3, model);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 
}

void loop() {
  // put your main code here, to run repeatedly:

  int vol1 = analogRead(IRP1);
  int vol2 = analogRead(IRP2);
  int vol3 = analogRead(IRP3);
 
  int dist1 = sensor1.distance();
  int dist2 = sensor2.distance();
  int dist3 = sensor3.distance();

  Serial.print(dist1);

  Serial.print(", ");

  Serial.print(dist2);
  
  Serial.print(", ");

  Serial.println(dist3);

  delay(300);

}