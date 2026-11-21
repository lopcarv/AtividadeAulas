void setup() {

  Serial.begin(9600);

}

void loop() {

  int segundos = millis() / 1000;

  Serial.print("Arduino ligado ha ");

  Serial.print(segundos);

  Serial.println(" segundos");

  delay(1000);

}