const int ledVerde = 8;
const int ledVermelho = 9;
const int botao = 2;

void setup() {
  pinMode(ledVerde, OUTPUT);
  pinMode(ledVermelho, OUTPUT);
  pinMode(botao, INPUT_PULLUP);
}

void loop() {

  if (digitalRead(botao) == LOW) {

    digitalWrite(ledVerde, HIGH);
    digitalWrite(ledVermelho, LOW);

  } else {

    digitalWrite(ledVerde, LOW);
    digitalWrite(ledVermelho, HIGH);

  }
}