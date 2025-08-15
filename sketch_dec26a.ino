void setup() {
  pinMode(2, INPUT);  
  pinMode(A5, INPUT); 
  pinMode(A4, INPUT);
  Serial.begin(9600);
}

void loop() {
  int A1 = analogRead(A4); 
  int A2 = analogRead(A5); 
/*

  Serial.print("X: ");
  Serial.print(A1);
  Serial.print(" | Y: ");
  Serial.println(A2);
*/
  
  int centerThreshold = 20;
  int centerX = 504; 
  int centerY = 522; 
  int x = analogRead(A3);  
  x= ceil(x/1023.0);
  int y = analogRead(A2);
  y= ceil(y/1023.0);
  int a = analogRead(A1);
  a= ceil(a/1023.0);
  int b = analogRead(A0);
  b= ceil(b/1023.0);
String strX = String(x);
String strY = String(y);
String strA = String(a);
String strB = String(b);
String con = strX + strY + strA + strB;
  if (abs(A1 - centerX) < centerThreshold && abs(A2 - centerY) < centerThreshold) {
    Serial.println("CENTER"+con);
  } else if (A1 > centerX + centerThreshold) {
    Serial.println("RIGHT"+con);
  } else if (A1 < centerX - centerThreshold) {
    Serial.println("LEFT"+con);
  } else if (A2 > centerY + centerThreshold) {
    Serial.println("DOWN"+con);
  } else if (A2 < centerY - centerThreshold) {
    Serial.println("UP"+con);
  }

  delay(100); 
}

