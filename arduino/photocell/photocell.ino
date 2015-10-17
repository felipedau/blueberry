//Pino analógico em que o sensor está conectado.
int Pino = 0;
//Variavel de leitura
int ValorSensor = 0;

//Método setup, executado uma vez ao ligar o Arduino.
void setup(){
//ativando o serial monitor
Serial.begin(9600);
}

//metodo loop, executado enquanto o arduino estiver ligado
void loop(){

ValorSensor = analogRead(Pino);

//Luminosidade baixa.
  if (valorSensor < 750) {
    apagaLeds();
    digitalWrite(ledVermelho,HIGH);
  }
  
  //Luminosidade média.
  if (valorSensor >= 750 && valorSensor <= 800) {
    apagaLeds();
    digitalWrite(ledAmarelo,HIGH);
  }
  
  //Luminosidade alta.
  if (valorSensor > 800) {
    apagaLeds();
    digitalWrite(ledVerde,HIGH);
  }
  
  Serial.println(ValorSensor);
  delay(2000);


}

void apagaLeds() {
  digitalWrite(ledVerde,LOW);
  digitalWrite(ledAmarelo,LOW);
  digitalWrite(ledVermelho,LOW);
}  