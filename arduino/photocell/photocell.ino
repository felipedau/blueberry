// pino analogico em que o sensor esta conectado
int sensor = 0;

// pinos digitais indicadores de nivel
int ledVermelho = 8;
int ledAmarelo = 10;
int ledVerde = 12;

int luminosidade = 0;

int intervalo = 5000;

// metodo setup, executado uma vez ao ligar o arduino
void setup() {
	//ativando o serial monitor
	Serial.begin(9600);
}

// metodo loop, executado enquanto o arduino estiver ligado
void loop() {
	luminosidade = analogRead(sensor);

	apagaLeds();
	if (luminosidade < 300) {
		// luminosidade baixa
		digitalWrite(ledVermelho, HIGH);
	} else if (luminosidade < 600) {
		// luminosidade media
		digitalWrite(ledAmarelo, HIGH);
	} else {
		// luminosidade alta
		digitalWrite(ledVerde, HIGH);
	}

	Serial.println(luminosidade);
	delay(intervalo);
}

void apagaLeds() {
	digitalWrite(ledVermelho, LOW);
	digitalWrite(ledAmarelo, LOW);
	digitalWrite(ledVerde, LOW);
}
