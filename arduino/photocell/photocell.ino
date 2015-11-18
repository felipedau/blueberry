// assign the light sensor to an analog pin
int sensor = 0;

// assign the LEDs that display the light level to digital pins
int ledLow = 8;
int ledMedium = 10;
int ledHigh = 12;

int level = 0;

// set an interval for the sensor read
int interval = 5000;

void setup() {
	// activate the serial monitor to send the light level
	Serial.begin(9600);
}

void loop() {
	level = analogRead(sensor);

	dimLeds();
	if (level < 300) {
		digitalWrite(ledLow, HIGH);
	} else if (level < 600) {
		digitalWrite(ledMedium, HIGH);
	} else {
		digitalWrite(ledHigh, HIGH);
	}

	// send the light level
	Serial.println(level);

	delay(interval);
}

void dimLeds() {
	digitalWrite(ledLow, LOW);
	digitalWrite(ledMedium, LOW);
	digitalWrite(ledHigh, LOW);
}
