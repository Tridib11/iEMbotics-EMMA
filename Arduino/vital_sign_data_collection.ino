#include <Wire.h>
#include <Adafruit_MLX90614.h>
#include <MAX30100_PulseOximeter.h>

// Define the sensors
Adafruit_MLX90614 mlx = Adafruit_MLX90614();
PulseOximeter pox;

// Timer for pulse oximeter
uint32_t tsLastReport = 0;

// Callback routine to update pulse and SpO2
void onPulseOximeterData(float spo2, float bpm) {
    Serial.print("SpO2: ");
    Serial.print(spo2);
    Serial.print(" % , ");
    Serial.print("Heart Rate: ");
    Serial.print(bpm);
    Serial.println(" bpm");
}

void setup() {
    Serial.begin(9600);
    Wire.begin();

    // Initialize the MLX90614 sensor
    if (!mlx.begin()) {
        Serial.println("Error connecting to MLX90614 sensor.");
        while (1);
    }

    // Initialize the MAX30100 Pulse Oximeter
    if (!pox.begin()) {
        Serial.println("Failed to initialize pulse oximeter.");
        while (1);
    }

    // Set callback for pulse oximeter data
    pox.setOnBeatDetectedCallback(onPulseOximeterData);

    Serial.println("Sensors initialized. Collecting data...");
}

void loop() {
    // Update pulse oximeter readings
    pox.update();

    // Read temperature from MLX90614
    float temp = mlx.readObjectTempC();
    Serial.print("Temperature: ");
    Serial.print(temp);
    Serial.println(" °C");

    // Send data to Raspberry Pi every 1 second
    if (millis() - tsLastReport > 1000) {
        tsLastReport = millis();

        // Transmit data over Serial
        Serial.print("DATA,");
        Serial.print(pox.getSpO2());
        Serial.print(",");
        Serial.print(pox.getHeartRate());
        Serial.print(",");
        Serial.print(temp);
        Serial.println();
    }

    delay(100); // Short delay for sensor stability
}
