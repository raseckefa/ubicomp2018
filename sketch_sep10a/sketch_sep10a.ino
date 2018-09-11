#include <Javino.h>
Javino javino;
String  strtemp = "temp=";
String  strstrtemp = "lumin=";
int val;
int tempPin = 1;
int pResistor = A0; 
int value;       
  
void setup() {
  pinMode(pResistor, INPUT);// Set pResistor - A0 pin as an input (optional)
  Serial.begin(9600);
}
void loop() {
  val = analogRead(tempPin);
  float mv = ( val/1024.0)*5000; 
  float cel = mv/10;
  cel = ((cel*10)*0.00466759) + 273;
  
  
  value = analogRead(pResistor);
  javino.sendmsg(strtemp+cel+"|"+strstrtemp+value);
  
  delay(1000);
}
