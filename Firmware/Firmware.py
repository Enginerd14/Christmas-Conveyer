
const int SENSOR_PIN = 2;   // PD2 (IR sensor D0)

const int AIN1 = 8;         // PB0
const int PWMA = 9;         // PB1 (PWM)

const int BIN1 = 10;        // PB2
const int BIN2 = 12;        // PB6
const int PWMB = 11;        // PB7 (PWM)

const int LED_PIN = 13;

void stopEndConveyor() {
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, LOW);
  analogWrite(PWMB, 0);
}

void moveEndConveyorLeft() {
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);
  analogWrite(PWMB, 180);
}

void moveEndConveyorRight() {
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);
  analogWrite(PWMB, 180);
}

void setup() {
  pinMode(SENSOR_PIN, INPUT);

  pinMode(AIN1, OUTPUT);
  pinMode(PWMA, OUTPUT);

  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);
  pinMode(PWMB, OUTPUT);

  pinMode(LED_PIN, OUTPUT);

  // Start main conveyor (always forward)
  digitalWrite(AIN1, HIGH);
  analogWrite(PWMA, 150);

  // Stop end conveyor at startup
  stopEndConveyor();
}


void loop() {
  int sensorState = digitalRead(SENSOR_PIN);

  if (sensorState == LOW) {
    digitalWrite(LED_PIN, HIGH);

    bool isCoal = true;

    if (isCoal) {
      moveEndConveyorLeft();   
    } else {
      moveEndConveyorRight();  
    }

    delay(700);    
    stopEndConveyor();
    delay(300);    
  } else {
    digitalWrite(LED_PIN, LOW);
  }
}
