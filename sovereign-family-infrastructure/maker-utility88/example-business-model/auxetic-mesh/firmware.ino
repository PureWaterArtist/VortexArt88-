#include <WiFi.h>
#include <HTTPClient.h>

// ============================================================================
// 📌 PHYSICAL HARDWARE PIN CONFIGURATION
// ============================================================================
#define IMU_SDA_PIN          21  // I2C Data line connected to MPU6050 Accelerometer
#define IMU_SCL_PIN          22  // I2C Clock line connected to MPU6050 Accelerometer
#define STRAIN_GAUGE_PIN     36  // Analog input line tracking integrated internal material strain
#define HALL_EFFECT_PIN      13  // Digital interrupt pin tracking active hub rotations (Odometer)

// ============================================================================
// 🎛️ OPERATIONAL SAFETY THRESHOLDS
// ============================================================================
const float CRITICAL_IMPACT_G  = 4.5;   // Structural limit threshold identifying a catastrophic curb smash
const int   MAX_STRAIN_LIMIT   = 880;   // Material deformation ceiling identifying structural elastomer fatigue
const long  TELEMETRY_INTERVAL = 30000; // 30-second localized logistics data synchronization timer

enum FleetTransitState { TRANSIT_NOMINAL, TRANSIT_HEAVY_VIBRATION, TRANSIT_ALERT_CRASH };
FleetTransitState core_health_state = TRANSIT_NOMINAL;

volatile int wheel_revolutions = 0;
unsigned long last_upload_timer = 0;
float instantaneous_velocity = 0.0;

// Interrupt Service Routine for Odometer Revolution Calculations
void IRAM_ATTR Log_Wheel_Rotation() {
  wheel_revolutions++;
}

void setup() {
  Serial.begin(115200);
  
  pinMode(STRAIN_GAUGE_PIN, INPUT);
  pinMode(HALL_EFFECT_PIN, INPUT_PULLUP);
  
  // Attach structural interrupt pin directly to tracking sensor
  attachInterrupt(digitalPinToInterrupt(HALL_EFFECT_PIN), Log_Wheel_Rotation, RISING);
  
  // Initialize internal I2C bus wiring communication links to the IMU module
  Wire.begin(IMU_SDA_PIN, IMU_SCL_PIN);
  Initialize_Internal_IMU();
  
  WiFi.begin("FLEET_LOGISTICS_NET", "IMMORTAL_GEOMETRY_88");
}

void loop() {
  // 1. DATA ACQUISITION FROM LOGISTICS IMU SENSOR
  float lateral_g_forces = Read_Accelerometer_Max_G();
  int structure_strain = analogRead(STRAIN_GAUGE_PIN);
  
  // Calculate rolling speedometer values based on odometer wheel pass pulses
  static unsigned long last_speed_check = 0;
  if (millis() - last_speed_check >= 1000) {
    noInterrupts();
    // Velocity calculation tracking a standard 700c wheel circumference (2.196 meters)
    instantaneous_velocity = (wheel_revolutions * 2.196) * 3.6; // Convert meters/sec to km/h
    wheel_revolutions = 0;
    interrupts();
    last_speed_check = millis();
  }

  // 2. DIAGNOSTIC EVALUATION LOGIC
  if (lateral_g_forces > CRITICAL_IMPACT_G) {
    core_health_state = TRANSIT_ALERT_CRASH;
  } else if (structure_strain > MAX_STRAIN_LIMIT) {
    core_health_state = TRANSIT_HEAVY_VIBRATION;
  } else {
    core_health_state = TRANSIT_NOMINAL;
  }

  // 3. WIRELESS LOGISTICS DATA TRANSMISSION LINK
  if (millis() - last_upload_timer >= TELEMETRY_INTERVAL) {
    Transmit_Fleet_Telemetry(lateral_g_forces, instantaneous_velocity, structure_strain);
    last_upload_timer = millis();
  }
  
  delay(10); // System cycle stabilizer
}

// ============================================================================
// 🧬 SUBSYSTEM RECONCILIATION DRIVERS
// ============================================================================

void Initialize_Internal_IMU() {
  Wire.beginTransmission(0x68); // MPU6050 standard I2C address
  Wire.write(0x6B);             // Power Management register address
  Wire.write(0);                // Wake up command token
  Wire.endTransmission(true);
}

float Read_Accelerometer_Max_G() {
  Wire.beginTransmission(0x68);
  Wire.write(0x3B); // Accel data register ingress point
  Wire.endTransmission(false);
  Wire.requestFrom(0x68, 6, true);
  
  int16_t raw_x = Wire.read() << 8 | Wire.read();
  int16_t raw_y = Wire.read() << 8 | Wire.read();
  int16_t raw_z = Wire.read() << 8 | Wire.read();
  
  // Convert mapping layout to real G-Force metrics under standard +/- 8G config
  float g_x = raw_x / 4096.0;
  float g_y = raw_y / 4096.0;
  float g_z = raw_z / 4096.0;
  
  return sqrt(g_x*g_x + g_y*g_y + g_z*g_z);
}

void Transmit_Fleet_Telemetry(float g_force, float speed_kmh, int material_strain) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin("http://fleet-hub.local");
    http.addHeader("Content-Type", "application/json");
    
    String payload = "{\"asset_id\":\"TIRE-CORE-700C-01\",\"impact_g\":" + String(g_force) + 
                     ",\"speed_kmh\":" + String(speed_kmh) + 
                     ",\"strain_raw\":" + String(material_strain) + 
                     ",\"health_state\":" + String(core_health_state) + "}";
                     
    int http_code = http.POST(payload);
    http.end();
  }
}
