int contador = 10; // 1. Definimos o valor inicial da contagem

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (contador >= 0) { // 2. Verificamos se ainda estamos no limite da contagem
    Serial.println(contador);
    contador--;        // 3. Decrementamos o valor a cada ciclo
  }
  
  delay(1000);         // Pausa de 1 segundo
}