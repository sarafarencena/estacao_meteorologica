#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>
#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
Adafruit_BMP280 bmp; // I2C

bool bmp_ok = false;

void setup() {
  Serial.begin(9600);
  dht.begin();

  bmp_ok = bmp.begin(0x76);

  if (!bmp_ok) {
    Serial.println("{\"erro\":\"BMP280 nao encontrado\"}");
  }
}

void loop() {
  float temp = dht.readTemperature();
  float umid = dht.readHumidity();

  if (!isnan(temp) && !isnan(umid)) {
    Serial.print("{");
    Serial.print("\"temperatura\":"); Serial.print(temp, 2);
    Serial.print(",\"umidade\":"); Serial.print(umid, 2);

    if (bmp_ok) {
      float pressao = bmp.readPressure() / 100.0; // hPa
      Serial.print(",\"pressao\":"); Serial.print(pressao, 2);
    }

    Serial.println("}");
  } else {
    Serial.println("{\"erro\":\"falha_leitura_dht\"}");
  }

  delay(5000);
}