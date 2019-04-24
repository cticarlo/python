
int deg = 0;
double rad;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (deg == 360)
    deg = 0;
  rad = deg*2*PI/360;
  Serial.println(sin(rad));
  deg+=3;
  delay(500);
}
