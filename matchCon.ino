byte serialByte;
// the setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(9600);
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(7, OUTPUT); // ethernet net pin 8, yellow
  pinMode(6, OUTPUT); // orange
  pinMode(4, OUTPUT); // white clear
  pinMode(2, OUTPUT); // purble brown

  /*
  Enable/disable, pin 6 - low = disabled, high = enabled.
  Driver/Auton, pin 2 - low = autonomous, high = driver code.
  LED Power, pin 4 - high = LED driver controller are on
  pin 8 = connected#
  */

}

void loop() {
  if (Serial.available()) {
    serialByte = Serial.read();
    // auto control
    if (serialByte=='A') {
      digitalWrite(8, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(4, HIGH);
      digitalWrite(2, LOW); // auto
    }
    // driver control
    if (serialByte=='B')
    {
      digitalWrite(8, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(4, HIGH);
      digitalWrite(2, HIGH); // driver
    }

    // clear all pins
    if (serialByte=='C')
    {
      digitalWrite(8, LOW);
      digitalWrite(6, LOw);
      digitalWrite(4, LOW);
      digitalWrite(2, LOW);
      delay(1000);
    }

    // disabled mode
    if (serialByte=='D')
    {
      digitalWrite(8, HIGH);
      digitalWrite(6, LOW); // disabled
      digitalWrite(4, HIGH);
      digitalWrite(2, HIGH);
      delay(1000);
    } // end if
  } // end while loop
} // end loop function
