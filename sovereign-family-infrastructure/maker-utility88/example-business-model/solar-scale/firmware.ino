#include <WiFi.h>
#include <HTTPClient.h>

// ============================================================================
// 📌 PHYSICAL HARDWARE PIN CONFIGURATION
// ============================================================================
#define PV_ADC_PIN          36  // Analog input tracking direct Photovoltaic cell voltage
#define TEG_ADC_PIN         39  // Analog input tracking Seebeck Thermoelectric voltage
#define PIEZO_ADC_PIN       34  // Analog input tracking PVDF Acoustic/Kinetic AC voltage
#define GRID_BYPASS_PIN     12  // GPIO driving the low-resistance MOSFET isolation switch
#define TELEMETRY_BUS_PIN   14  // Common single-wire serial mesh data communication line

// ============================================================================
// 🎛️ OPERATIONAL ENERGY THRESHOLDS
// ============================================================================
const float MIN_SAFE_VOLTAGE   = 0.45;  // Baseline generation floor. Dropping below isolates the node.
const float VOLTAGE_CONVERSION = 5.0;   // Scaling reference parameter mapping standard 12-bit ADC reads
const unsigned long SYNC_RATE  = 20000; // 20-second array node telemetry interval

// System Grid State Management
enum GridStatus { ENERGY_NOMINAL_DAY, ENERGY_NOMINAL_NIGHT, ENERGY_NODE_FAULT_ISOLATED };
GridStatus array_node_state = ENERGY_NOMINAL_DAY;

unsigned long last_sync_timestamp = 0;
float current_total_output_v = 0.0;

void setup() {
  Serial.begin(115200);
  
  pinMode(PV_ADC_PIN, INPUT);
  pinMode(TEG_ADC_PIN, INPUT);
  pinMode(PIEZO_ADC_PIN, INPUT);
  pinMode(GRID_BYPASS_PIN, OUTPUT);
  pinMode(TELEMETRY_BUS_PIN, INPUT_PULLUP);
  
  // Connect Tile into the Shared Parallel Array Bus at startup (Keep bypass FET off)
  digitalWrite(GRID_BYPASS_PIN, LOW);
  
  WiFi.begin("MATRIX_SOLAR_MESH", "IMMORTAL_GEOMETRY_88");
}

void loop() {
  // 1. DATA ACQUISITION FROM THE MULTI-MATERIAL ENERGY MATRIX
  float pv_voltage    = (analogRead(PV_ADC_PIN) / 4095.0) * VOLTAGE_CONVERSION;
  float teg_voltage   = (analogRead(TEG_ADC_PIN) / 4095.0) * VOLTAGE_CONVERSION;
  float piezo_voltage = (analogRead(PIEZO_ADC_PIN) / 4095.0) * VOLTAGE_CONVERSION;
  
  // Compute total combined additive voltage generation footprint
  current_total_output_v = pv_voltage + teg_voltage + piezo_voltage;

  // 2. SELF-HEALING AUTOMATED SAFETY ROUTING MATRIX
  if (current_total_output_v < MIN_SAFE_VOLTAGE) {
    // Current drop indicates severe material soot structural failure or total shadow blockage.
    // Trigger immediate hardware bypass isolation to keep the shared power rails from dragging down.
    array_node_state = ENERGY_NODE_FAULT_ISOLATED;
    digitalWrite(GRID_BYPASS_PIN, HIGH); // Force low-resistance MOSFET to bypass the node
  } 
  else if (pv_voltage < teg_voltage) {
    // Nighttime condition: Solar cell is down, but Seebeck and Acoustic grids are actively harvesting
    array_node_state = ENERGY_NOMINAL_NIGHT;
    digitalWrite(GRID_BYPASS_PIN, LOW); // Retain active bus injection loop
  } 
  else {
    // Daytime condition: Photovoltaic core is acting as primary energy generator
    array_node_state = ENERGY_NOMINAL_DAY;
    digitalWrite(GRID_BYPASS_PIN, LOW); // Retain active bus injection loop
  }

  // 3. SECURE TELEMETRY TRANSMISSION LOGGING
  if (millis() - last_sync_timestamp >= SYNC_RATE) {
    Broadcast_Node_Telemetry(pv_voltage, teg_voltage, piezo_voltage);
    last_sync_timestamp = millis();
  }
  
  delay(50); // Clock stabilizer loop
}

// ============================================================================
// 🧬 SUBSYSTEM RECONCILIATION DRIVERS
// ============================================================================

void Broadcast_Node_Telemetry(float pv, float teg, float piezo) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin("http://grid-coordinator.local");
    http.addHeader("Content-Type", "application/json");
    
    String json_payload = "{\"node_serial\":\"SCALE-700X-01\",\"pv_v\":" + String(pv) + 
                          ",\"teg_v\":" + String(teg) + 
                          ",\"piezo_v\":" + String(piezo) + 
                          ",\"total_combined_v\":" + String(current_total_output_v) + 
                          ",\"grid_state\":" + String(array_node_state) + "}";
                          
    int http_response_code = http.POST(json_payload);
    http.end();
  }
}
