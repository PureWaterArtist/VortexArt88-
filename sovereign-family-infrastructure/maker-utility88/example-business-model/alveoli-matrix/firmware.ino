#include <WiFi.h>
#include <HTTPClient.h>

// ============================================================================
// 📌 PHYSICAL HARDWARE PIN CONFIGURATION
// ============================================================================
#define ION_GENERATOR_PIN    12  // PWM signal driving the High-Voltage Low-Current Static Generator
#define AQI_PM25_RX_PIN      16  // Serial input connection from PM2.5 Laser Particle Sensor
#define AQI_PM25_TX_PIN      17  // Serial output connection to PM2.5 Laser Particle Sensor
#define THERMISTOR_BASE_PIN  34  // Analog thermistor pin monitoring lower room intake air temp
#define THERMISTOR_TOP_PIN   35  // Analog thermistor pin monitoring upper chimney exhaust temp

// ============================================================================
// 🎛️ OPERATIONAL SAFETY THRESHOLDS
// ============================================================================
const int CRITICAL_PM25_LIMIT = 150;   // Trigger index warning value (μg/m³). Triggers maximum ionization charge.
const long METRIC_INTERVAL    = 15000; // 15-second data upload timer

enum OperationalState { STATE_STANDBY_CLEAN, STATE_ACTIVE_FILTRATION, STATE_ALERT_HAZARD };
OperationalState air_quality_state = STATE_STANDBY_CLEAN;

int current_pm25_value = 0;
unsigned long last_transmission = 0;

void setup() {
  Serial.begin(115200);
  Serial1.begin(9600, SERIAL_8N1, AQI_PM25_RX_PIN, AQI_PM25_TX_PIN); // Laser sensor serial link
  
  pinMode(ION_GENERATOR_PIN, OUTPUT);
  pinMode(THERMISTOR_BASE_PIN, INPUT);
  pinMode(THERMISTOR_TOP_PIN, INPUT);
  
  // Initialize safe baseline charge across the conductive frame (40% duty cycle)
  analogWrite(ION_GENERATOR_PIN, 102); 
  
  WiFi.begin("MATRIX_FOUNDRY_NET", "IMMORTAL_GEOMETRY_88");
}

void loop() {
  // 1. DATA ACQUISITION FROM AIRBORNE LASER SENSOR
  if (Serial1.available()) {
    current_pm25_value = Process_Laser_Sensor_Data();
  }

  // 2. TRACK THERMISTOR DELTAS TO PROVE CONVECTIVE PASSIVE AIR DISPLACEMENT
  float base_temp = Read_Thermal_Celsius(THERMISTOR_BASE_PIN);
  float top_temp = Read_Thermal_Celsius(THERMISTOR_TOP_PIN);
  float thermal_delta = abs(top_temp - base_temp);

  // 3. AUTOMATED CHARGE BALANCING MATRIX
  if (current_pm25_value > CRITICAL_PM25_LIMIT) {
    air_quality_state = STATE_ALERT_HAZARD;
    analogWrite(ION_GENERATOR_PIN, 255); // Maximize frame static charge to pull massive particle dumps
  } else if (current_pm25_value > 35) {
    air_quality_state = STATE_ACTIVE_FILTRATION;
    analogWrite(ION_GENERATOR_PIN, 178); // 70% static intensity charge
  } else {
    air_quality_state = STATE_STANDBY_CLEAN;
    analogWrite(ION_GENERATOR_PIN, 76);  // Drop to low-power maintenance background charge
  }

  // 4. DATA TELEMETRY LOG TRANSMISSION
  if (millis() - last_transmission >= METRIC_INTERVAL) {
    Send_Purifier_Telemetry(current_pm25_value, thermal_delta);
    last_transmission = millis();
  }

  delay(50); // System cycle headroom clock
}

// ============================================================================
// 🧬 SUBSYSTEM RECONCILIATION DRIVERS
// ============================================================================

int Process_Laser_Sensor_Data() {
  uint8_t buffer[32];
  uint8_t idx = 0;
  
  while (Serial1.available() && idx < 32) {
    buffer[idx++] = Serial1.read();
  }
  
  // Standard Plantower PM2.5 transmission data packet parsing logic check
  if (buffer[0] == 0x42 && buffer[1] == 0x4d) {
    int pm25_concentration = (buffer[12] << 8) + buffer[13]; // Extract concentration indexing
    return pm25_concentration;
  }
  return current_pm25_value;
}

float Read_Thermal_Celsius(int pin) {
  int raw = analogRead(pin);
  // Standard Steinhart-Hart equation parsing to read precise analog temperature data
  float resistance = 10000.0 / (4095.0 / raw - 1.0);
  float steinhart;
  steinhart = resistance / 10000.0;
  steinhart = log(steinhart);
  steinhart /= 3950.0; // Beta coefficient
  steinhart += 1.0 / (25.0 + 273.15); // Room baseline reference
  steinhart = 1.0 / steinhart;
  steinhart -= 273.15;
  return steinhart;
}

void Send_Purifier_Telemetry(int pm25, float delta) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin("http://farm-controller.local");
    http.addHeader("Content-Type", "application/json");
    
    String json = "{\"device_id\":\"ALVEOLI-01\",\"pm25_ugm3\":" + String(pm25) + 
                  ",\"thermal_delta_c\":" + String(delta) + 
                  ",\"system_state\":" + String(air_quality_state) + "}";
                  
    int response = http.POST(json);
    http.end();
  }
}
