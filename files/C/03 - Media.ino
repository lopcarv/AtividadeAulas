float nota1 = 8.5; 
float nota2 = 7.0; 
float media; 
      
void setup() { 
      
      Serial.begin(9600); 
      
      media = (nota1 + nota2) / 2; 
      
      Serial.print("Media = "); 
    
      Serial.println(media); 
      
     } 
      
 	void loop() { 
      
     }
