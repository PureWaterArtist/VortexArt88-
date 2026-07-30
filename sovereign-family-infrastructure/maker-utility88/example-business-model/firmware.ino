#include <Adafruit_NeoPixel.h>

#define LED_PIN_BOTTOM    2   
#define LED_PIN_TOP       3   
#define NUM_LEDS          8   
#define MOTOR_PWM_PIN     4   
#define MIC_ANALOG_PIN    26  
#define TOUCH_SENSE_PIN   15  

const int TOUCH_THRESHOLD   = 400;   
const int BABY_CRY_VOLTS     = 650;   
const long CHILL_OUT_TIME   = 45000; 

enum SystemState { SLEEP_NIGHTLIGHT, VORTEX_ACTIVE, INFANT_SOOTHE };
SystemState current_state = SLEEP_NIGHTLIGHT;
int active_color_profile = 0; 
unsigned long soothe_start_timer = 0;

Adafruit_NeoPixel RingBottom(NUM_LEDS, LED_PIN_BOTTOM, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel RingTop(NUM_LEDS, LED_PIN_TOP, NEO_GRB + NEO_KHZ800);

void setup() {
  pinMode(MOTOR_PWM_PIN, OUTPUT);
  pinMode(TOUCH_SENSE_PIN, INPUT);
  pinMode(MIC_ANALOG_PIN, INPUT);
  RingBottom.begin();
  RingTop.begin();
  Execute_System_Drive(40, 255, 120, 0); 
}

void loop() {
  int touch_reading = readCapacitivePin(TOUCH_SENSE_PIN);
  if (touch_reading > TOUCH_THRESHOLD) {
    delay(200); 
    Cycle_System_Modes();
  }
  switch (current_state) {
    case SLEEP_NIGHTLIGHT:
      Execute_System_Drive(20, 100, 35, 0); 
      if (analogRead(MIC_ANALOG_PIN) > BABY_CRY_VOLTS) {
        current_state = INFANT_SOOTHE;
        soothe_start_timer = millis();
      }
      break;
    case VORTEX_ACTIVE:
      Manage_Active_Visuals();
      break;
    case INFANT_SOOTHE:
      int pulse = (sin(millis() / 1500.0) * 30) + 70; 
      Execute_System_Drive(pulse, 0, 150, 200); 
      if (millis() - soothe_start_timer > CHILL_OUT_TIME) {
        current_state = SLEEP_NIGHTLIGHT;
      }
      break;
  }
  delay(10); 
}

void Execute_System_Drive(int motor_speed, int r, int g, int b) {
  analogWrite(MOTOR_PWM_PIN, map(motor_speed, 0, 100, 0, 255));
  for(int i=0; i<NUM_LEDS; i++) { RingBottom.setPixelColor(i, RingBottom.Color(r, g, b)); }
  for(int i=0; i<NUM_LEDS; i++) {
    if (active_color_profile == 2 && current_state == VORTEX_ACTIVE) {
      RingTop.setPixelColor(i, RingTop.Color(0, 120, 255)); 
    } else {
      RingTop.setPixelColor(i, RingTop.Color(r, g, b));
    }
  }
  RingBottom.show(); RingTop.show();
}

void Cycle_System_Modes() {
  if (current_state == SLEEP_NIGHTLIGHT) { current_state = VORTEX_ACTIVE; active_color_profile = 0; }
  else if (current_state == VORTEX_ACTIVE) {
    active_color_profile++;
    if (active_color_profile > 2) { current_state = SLEEP_NIGHTLIGHT; }
  } else if (current_state == INFANT_SOOTHE) { current_state = SLEEP_NIGHTLIGHT; }
}

void Manage_Active_Visuals() {
  if (active_color_profile == 0) { Execute_System_Drive(60, 255, 110, 0); } 
  else if (active_color_profile == 1) {
    int dynamic_green = (sin(millis() / 800.0) * 50) + 150;
    Execute_System_Drive(75, 0, dynamic_green, 180);
  } 
  else if (active_color_profile == 2) { Execute_System_Drive(95, 240, 180, 0); }
}

int readCapacitivePin(int pinToMeasure) {
  volatile uint32_t* reg = portInputRegister(digitalPinToPort(pinToMeasure));
  uint32_t mask = digitalPinToBitMask(pinToMeasure);
  int count = 0;
  pinMode(pinToMeasure, OUTPUT);
  digitalWrite(pinToMeasure, LOW);
  delay(1);
  noInterrupts();
  pinMode(pinToMeasure, INPUT);
  while ((*reg & mask) == 0 && count < 2000) { count++; }
  interrupts();
  return count;
}
