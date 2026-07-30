#include <Adafruit_NeoPixel.h>

// ==========================================
// 📌 PHYSICAL HARDWARE PIN CONFIGURATION
// ==========================================
#define LED_PIN_BOTTOM    2   // Data pin for Lower NeoPixel LED Ring
#define LED_PIN_TOP       3   // Data pin for Upper NeoPixel LED Ring
#define NUM_LEDS          8   // Number of LEDs per individual ring

#define MOTOR_PWM_PIN     4   // PWM speed control wire to 5V Brushless Driver Board
#define MIC_ANALOG_PIN    26  // Analog input pin from MAX4466 Sound Sensor
#define TOUCH_SENSE_PIN   15  // Input pin wired to the Conductive Carbon-Fiber 3D Pillar

// ==========================================
// 🎛️ OPERATIONAL SENSING PARAMETERS
// ==========================================
const int TOUCH_THRESHOLD   = 400;   // Trigger limit for Capacitive Touch (Adjust to filament conductivity)
const int BABY_CRY_VOLTS     = 650;   // Amplitude threshold identifying a high-frequency baby cry
const long CHILL_OUT_TIME   = 45000; // 45-second soothing cycle before dropping back to low-power sleep

// System State Architecture
enum SystemState { SLEEP_NIGHTLIGHT, VORTEX_ACTIVE, INFANT_SOOTHE };
SystemState current_state = SLEEP_NIGHTLIGHT;

int active_color_profile = 0; // 0: Amber Glow, 1: Oceanic Matrix, 2: Kinetic Hourglass Aurora
unsigned long soothe_start_timer = 0;

// Initialize Dual-Zone Lighting Matrices
Adafruit_NeoPixel RingBottom(NUM_LEDS, LED_PIN_BOTTOM, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel RingTop(NUM_LEDS, LED_PIN_TOP, NEO_GRB + NEO_KHZ800);

void setup() {
  pinMode(MOTOR_PWM_PIN, OUTPUT);
  pinMode(TOUCH_SENSE_PIN, INPUT);
  pinMode(MIC_ANALOG_PIN, INPUT);
  
  RingBottom.begin();
  RingTop.begin();
  
  // Set Safe Startup Baseline (Low Speed, Soft Calming Amber)
  Execute_System_Drive(40, 255, 120, 0); 
}

void loop() {
  // 1. EVALUATE PASSIVE INTERACTIVE TOUCH CONTROL
  int touch_reading = readCapacitivePin(TOUCH_SENSE_PIN);
  if (touch_reading > TOUCH_THRESHOLD) {
    delay(200); // Mechanical debounce buffer
    Cycle_System_Modes();
  }

  // 2. STATE MACHINE ROUTING AND SMART MONITORING
  switch (current_state) {
    
    case SLEEP_NIGHTLIGHT:
      // Keep motor whisper-quiet; project a gentle, breathing soft amber perimeter
      Execute_System_Drive(20, 100, 35, 0); 
      
      // Monitor environment for high-amplitude nursery sound disruptions
      if (analogRead(MIC_ANALOG_PIN) > BABY_CRY_VOLTS) {
        current_state = INFANT_SOOTHE;
        soothe_start_timer = millis();
      }
      break;

    case VORTEX_ACTIVE:
      // High-performance operational state driven by active user color selections
      Manage_Active_Visuals();
      break;

    case INFANT_SOOTHE:
      // Smart Auto-Intervention Mode triggered by sound sensor
      // Slowly pulse the kinetic vortex and cast a deep, calming wave-spectrum light
      int pulse = (sin(millis() / 1500.0) * 30) + 70; // Smooth wave interpolation
      Execute_System_Drive(pulse, 0, 150, 200); // Teal visual spectrum profile
      
      // Check if soothing timeline is completed, then return to low-power monitoring
      if (millis() - soothe_start_timer > CHILL_OUT_TIME) {
        current_state = SLEEP_NIGHTLIGHT;
      }
      break;
  }
  delay(10); // System cycle headroom
}

// ==========================================
// 🛠️ SUBSYSTEM DRIVER EXTRACTION LOGIC
// ==========================================

// Pure Parametric Control over Hardware Outputs
void Execute_System_Drive(int motor_speed, int r, int g, int b) {
  // Push standard analog step out to Brushless ESC Driver Matrix
  analogWrite(MOTOR_PWM_PIN, map(motor_speed, 0, 100, 0, 255));
  
  // Set all physical LED nodes across the bottom matrix
  for(int i=0; i<NUM_LEDS; i++) {
    RingBottom.setPixelColor(i, RingBottom.Color(r, g, b));
  }
  
  // Inverse phase lighting for the upper cap matrix to achieve dual-color hourglass mix
  for(int i=0; i<NUM_LEDS; i++) {
    if (active_color_profile == 2 && current_state == VORTEX_ACTIVE) {
      RingTop.setPixelColor(i, RingTop.Color(0, 120, 255)); // Lock Top to Sapphire Blue
    } else {
      RingTop.setPixelColor(i, RingTop.Color(r, g, b));
    }
  }
  
  RingBottom.show();
  RingTop.show();
}

// Manages User Iterations across Profile Selections
void Cycle_System_Modes() {
  if (current_state == SLEEP_NIGHTLIGHT) {
    current_state = VORTEX_ACTIVE;
    active_color_profile = 0;
  } else if (current_state == VORTEX_ACTIVE) {
    active_color_profile++;
    if (active_color_profile > 2) {
      current_state = SLEEP_NIGHTLIGHT; // Loop complete, drop back to safety standby
    }
  } else if (current_state == INFANT_SOOTHE) {
    current_state = SLEEP_NIGHTLIGHT; // Manual parent tap immediately cancels auto-soothing
  }
}

// Visual Matrix Routing
void Manage_Active_Visuals() {
  if (active_color_profile == 0) {
    // Amber Horizon Profile (Motor running at stable 60% velocity)
    Execute_System_Drive(60, 255, 110, 0);
  } 
  else if (active_color_profile == 1) {
    // Oceanic Rheoscopic Wave (Cascading Greens and Teals)
    int dynamic_green = (sin(millis() / 800.0) * 50) + 150;
    Execute_System_Drive(75, 0, dynamic_green, 180);
  } 
  else if (active_color_profile == 2) {
    // Hourglass Convergence (Max Kinetic Tornado. Base is Gold, Top is Sapphire)
    Execute_System_Drive(95, 240, 180, 0); 
  }
}

// Software-Defined Capacitive Sensing (Eliminates external IC hardware dependency)
int readCapacitivePin(int pinToMeasure) {
  volatile uint32_t* reg = portInputRegister(digitalPinToPort(pinToMeasure));
  uint32_t mask = digitalPinToBitMask(pinToMeasure);
  int count = 0;
  
  pinMode(pinToMeasure, OUTPUT);
  digitalWrite(pinToMeasure, LOW);
  delay(1);
  
  // Drive floating charge across the structural 3D polymer body
  noInterrupts();
  pinMode(pinToMeasure, INPUT);
  while ((*reg & mask) == 0 && count < 2000) { count++; }
  interrupts();
  
  return count;
}
