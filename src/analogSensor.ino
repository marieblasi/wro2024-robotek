#include "SharpIR.h"
#include "QTRSensors.h"

#define model 1080

#define IRP1 A0
#define IRP2 A1
#define IRP3 A2

QTRSensors qtra;

uint16_t sensor_values[2];

SharpIR sensor1 = SharpIR(IRP1, model);
SharpIR sensor2 = SharpIR(IRP2, model);
SharpIR sensor3 = SharpIR(IRP3, model);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 

  qtra.setTypeAnalog();
  qtra.setSensorPins((const uint8_t[]){A3, A4}, 2);

}

void loop() {
  // put your main code here, to run repeatedly:

  qtra.read(sensor_values);

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

  Serial.print(dist3);

  Serial.print(", ");

  Serial.print(sensor_values[0]);
  
  Serial.print(", ");

  Serial.println(sensor_values[1]);

  delay(300);

}