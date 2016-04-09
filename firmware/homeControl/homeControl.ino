int i = 0;
byte c;
byte buff[5] = {100, 100, 100, 100, 100};

void setup()
{
  Serial.begin(9600);
  for (i = 0; i < 14; i++)
    pinMode(i,OUTPUT);
}

void loop()
{
  if (Serial.available()) {
    c = Serial.read();
    for (i = 0; i < 4; i++) {
      buff[i] = buff[i + 1];
    }
    buff[4] = c;
    if (buff[0] == 200 && buff[4] == 200) {
        digitalWrite(buff[2],buff[3]);
    }
  }
}

