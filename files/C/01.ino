// Declaração de uma variável global do tipo String chamada "nomePessoa"
String nomePessoa = "Luis"; 

void setup() { 
  Serial.begin(9600); 
  Serial.println("Sistema iniciado"); 
  
  // Usando a variável no comando de saída
  Serial.print("Meu nome é "); 
  Serial.println(nomePessoa); 
}

void loop() { 
}
