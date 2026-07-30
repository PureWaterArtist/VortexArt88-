#include <WiFi.h>
#include <HTTPClient.h>

// ============================================================================
// 📌 PHYSICAL HARDWARE PIN CONFIGURATION
// ============================================================================
#define BYPASS_VALVE_PIN     5   // GPIO control wire to 5V Motorized Diverter Ball Valve
#define FLOW_SENSOR_PIN      4   // Digital pulse input from G1/2" Water Flow Sensor
#define TURBIDITY_PIN        26  // Analog input from Hydro-Optical Turbidity Sensor
#define PRESSURE_SENSOR_PIN  27  // Analog input from Solid-State Hydraulic Pressure Transducer

// ============================================================================
// 🎛️ OPERATIONAL SAFETY THRESHOLDS
// ============================================================================
const float MAX_SAFE_PRESSURE  = 2.2;   // Critical pressure ceiling (PSI). Higher indicates a downstream block.
const int   CRITICAL_TURBIDITY = 850;   // Maximum particulate density limit before auto-bypassing heavy waste.
const unsigned long POLLING_INT = 10000; // 10-second data telemetry loop interval

// System State Architecture
enum SystemState { STATUS_NOMINAL, STATUS_HEAVY_WASTE_BYPASS, STATUS_CRITICAL_BLOCKAGE };
SystemState current_state = STATUS_NOMINAL;

// Telemetry Data Variables
volatile int flow_pulse_count = 0;
unsigned long last_telemetry_time = 0;
float calculated_flow_rate = 0.0; 

// Interrupt Service Routine for Flow Pulse Counting
void IRAM_ATTR Link_Flow_Pulse() {
  flow_pulse_count++;
}

void setup() {
  Serial.begin(115200);
  
  pinMode(BYPASS_VALVE_PIN, OUTPUT);
  pinMode(FLOW_SENSOR_PIN, INPUT_PULLUP);
  pinMode(TURBIDITY_PIN, INPUT);
  pinMode(PRESSURE_SENSOR_PIN, INPUT);
  
  // Attach hardware interrupt directly to the flow rotor pin for real-time tracking
  attachInterrupt(digitalPinToInterrupt(FLOW_SENSOR_PIN), Link_Flow_Pulse, RISING);
  
  // Initialize Valve Position to NOMINAL (Closed Bypass Route / Open Filtration Path)
  digitalWrite(BYPASS_VALVE_PIN, LOW); 
  
  WiFi.begin("MATRIX_FOUNDRY_NET", "IMMORTAL_GEOMETRY_88");
}

void loop() {
  // 1. EXECUTE REAL-TIME HYDRAULIC SENSING
  float dynamic_pressure = Read_Hydraulic_Pressure(PRESSURE_SENSOR_PIN);
  int fluid_turbidity = analogRead(TURBIDITY_PIN);
  
  // Calculate flow rate based on accumulated pulses over a 1-second sample window
  static unsigned long last_flow_sample = 0;
  if (millis() - last_flow_sample >= 1000) {
    noInterrupts(); // Sandbox memory during calculation
    calculated_flow_rate = (flow_pulse_count / 7.5); // Standard G1/2 Flow Sensor conversion factor (L/min)
    flow_pulse_count = 0;
    interrupts();
    last_flow_sample = millis();
  }

  // 2. STATE MACHINE LOGIC MATRIX
  if (dynamic_pressure > MAX_SAFE_PRESSURE) {
    current_state = STATUS_CRITICAL_BLOCKAGE;
  } else if (fluid_turbidity > CRITICAL_TURBIDITY) {
    current_state = STATUS_HEAVY_WASTE_BYPASS;
  } else {
    current_state = STATUS_NOMINAL;
  }

  // 3. MECHANICAL VALVING INTERVENTION EXECUTION
  switch (current_state) {
    
    case STATUS_NOMINAL:
      digitalWrite(BYPASS_VALVE_PIN, LOW); // Retain filtration flow route
      break;

    case STATUS_HEAVY_WASTE_BYPASS:
      digitalWrite(BYPASS_VALVE_PIN, HIGH); // Open bypass to protect internal sharkskin chevrons
      break;

    case STATUS_CRITICAL_BLOCKAGE:
      digitalWrite(BYPASS_VALVE_PIN, HIGH); // Force immediate emergency drainage diversion
      break;
  }

  // 4. FOUNDRY TELEMETRY TRANSMISSION LINK
  if (millis() - last_telemetry_time >= POLLING_INT) {
    Transmit_Telemetry_Data(dynamic_pressure, calculated_flow_rate, fluid_turbidity);
    last_telemetry_time = millis();
  }
  
  delay(20); // System cycle stabilizer
}

// ============================================================================
// 🧬 SUBSYSTEM RECONCILIATION DRIVERS
// ============================================================================

float Read_Hydraulic_Pressure(int pin) {
  int raw_analog = analogRead(pin);
  float voltage = (raw_analog / 4095.0) * 3.3;
  // Convert 0.5V - 4.5V output mapping standard to 0-15 PSI transducer limits
  float psi = (voltage - 0.5) * (15.0 / 4.0);
  return max(0.0f, psi);
}

void Transmit_Telemetry_Data(float psi, float flow, int turbidity) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin("http://farm-controller.local");
    http.addHeader("Content-Type", "application/json");
    
    String json_payload = "{\"device_id\":\"STRATA-01\",\"pressure_psi\":" + String(psi) + 
                          ",\"flow_lmin\":" + String(flow) + 
                          ",\"turbidity_raw\":" + String(turbidity) + 
                          ",\"state\":" + String(current_state) + "}";
                          
    int http_response_code = http.POST(json_payload);
    http.end();
  }
}
