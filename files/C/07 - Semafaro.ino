int verde = 13;
int amarelo = 12;
int vermelho = 11;

void setup() {

  pinMode(verde, OUTPUT);
  pinMode(amarelo, OUTPUT);
  pinMode(vermelho, OUTPUT);

}

void loop() {

  digitalWrite(verde, HIGH);
  delay(3000);
  digitalWrite(verde, LOW);

  digitalWrite(amarelo, HIGH);
  delay(2000);
  digitalWrite(amarelo, LOW);

  digitalWrite(vermelho, HIGH);
  delay(3000);
  digitalWrite(vermelho, LOW);

}

