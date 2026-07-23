#!/usr/bin/env python3
import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
canvas = np.zeros((1080, 1920, 3), dtype=np.uint8)
canvas[:] = [4, 2, 1]

cv2.line(canvas, (960, 0), (960, 1080), (53, 41, 30), 3)
for x in range(0, 1920, 60):
    if x != 960: cv2.line(canvas, (x, 0), (x, 1080), (14, 9, 4), 1)
for y in range(0, 1080, 60):
    cv2.line(canvas, (0, y), (1920, y), (14, 9, 4), 1)

# Left Panel
cv2.rectangle(canvas, (40, 140), (920, 1000), (20, 20, 127), -1)
cv2.rectangle(canvas, (40, 140), (920, 1000), (44, 44, 239), 2)
cv2.putText(canvas, "CENTRAL SOFTWARE INFRA", (70, 200), font, 1.1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(canvas, "X SYSTEM CRITICAL LIABILITIES", (70, 250), font, 0.9, (68, 68, 239), 2, cv2.LINE_AA)
cv2.line(canvas, (70, 280), (890, 280), (44, 44, 239), 2)

left_lines = [
    "* SECTOR BALANCING CONTROL  : DIGITAL MICROCHIP ALGORITHMS",
    "* LOGIC INTERLINK CODES     : FRAGILE MAINWARE DATA LOOPS",
    "* SURGE MISMATCH OUTCOME    : SEVERE SYSTEM PHASE DISRUPTION",
    "* MALICIOUS EXPLOIT ROUTE   : CYBER ATTACK BACKDOOR INTRUSION",
    "* NETWORK FAILURE SHOCK PROFILE: CASCADING MULTI-STATE BLACKOUT",
    "* THERMAL OVERHEATING LIMITS: FANS & RECURRING COOLING COSTS",
    "* LOGIC UPDATE SCHEDULING   : CONTINUOUS EXPENSIVE SOFTWARE BUGS"
]
y_pos = 350
for line in left_lines:
    cv2.putText(canvas, line, (70, y_pos), font, 0.72, (200, 200, 255), 2, cv2.LINE_AA)
    y_pos += 80

# Right Panel
cv2.rectangle(canvas, (1000, 140), (1880, 1000), (32, 78, 14), -1)
cv2.rectangle(canvas, (1000, 140), (1880, 1000), (129, 217, 16), 2)
cv2.putText(canvas, "SOLID-STATE FLUIDIC SWITCHES", (1030, 200), font, 1.1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(canvas, "O IMMORTAL PARITY ADVANTAGE", (1030, 250), font, 0.9, (244, 242, 0), 2, cv2.LINE_AA)
cv2.line(canvas, (1030, 280), (1850, 280), (129, 217, 16), 2)

right_lines = [
    "* SECTOR BALANCING CONTROL  : NATURAL LAWS OF THERMODYNAMICS",
    "* LOGIC INTERLINK ROUTING   : PURE GEOMETRIC CHANNEL INTERACT",
    "* DYNAMIC GRID SPIKE INPUTS : AUTOMATIC JOULE HEAT TRIGGER ($I^2R$)",
    "* BALANCING ROUTE MECHANICS : SEEBECK-CURIE FLUIDIC MOVEMENT",
    "* FLUID MOVEMENT SPEED RATE : 3.82 m/s AUTONOMOUS VELOCITY",
    "* MALICIOUS EXPLOIT ROUTE   : 100% UN-HACKABLE ZERO DIGITAL LINES",
    "* NETWORK DETOUR SAFE WALL  : SOLID FLUIDIC SWITCH DETOUR AT 65°C"
]
y_pos = 350
for line in right_lines:
    cv2.putText(canvas, line, (1030, y_pos), font, 0.72, (230, 255, 230), 2, cv2.LINE_AA)
    y_pos += 80

cv2.rectangle(canvas, (0, 0), (1920, 80), (12, 10, 6), -1)
cv2.putText(canvas, "PROJECT RESONANT INFRASTRUCTURE // SOLID-STATE FLUIDIC LOAD-BALANCING // SHIELD v1.0.0", (30, 50), font, 0.85, (245, 158, 11), 2, cv2.LINE_AA)

cv2.imwrite("grid88-vs-legacy-switching.png", canvas)
print("SUCCESS: Infographic 5 (Switching) generated perfectly.")
