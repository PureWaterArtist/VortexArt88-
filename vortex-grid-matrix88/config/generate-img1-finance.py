#!/usr/bin/env python3
import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

# 🪐 1. INITIALIZE CANVAS MATRIX (1920x1080 Full HD, 16:9)
canvas = np.zeros((1080, 1920, 3), dtype=np.uint8)
canvas[:] = [4, 2, 1]  # Deep near-black hex (#010204)

# 📐 2. DRAW CENTER DIVISION AND METROLOGY GRID OVERLAYS
cv2.line(canvas, (960, 0), (960, 1080), (53, 41, 30), 3)
for x in range(0, 1920, 60):
    if x != 960: cv2.line(canvas, (x, 0), (x, 1080), (14, 9, 4), 1)
for y in range(0, 1080, 60):
    cv2.line(canvas, (0, y), (1920, y), (14, 9, 4), 1)

# ❌ 3. LEFT PANEL: LEGACY UNITED STATES INFRASTRUCTURE LIABILITIES
cv2.rectangle(canvas, (40, 140), (920, 1000), (20, 20, 127), -1)
cv2.rectangle(canvas, (40, 140), (920, 1000), (44, 44, 239), 2)
cv2.putText(canvas, "LEGACY UNITED STATES GRID BASELINE", (70, 200), font, 1.1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(canvas, "X SYSTEM CRITICAL LIABILITIES PROFILE", (70, 250), font, 0.9, (68, 68, 239), 2, cv2.LINE_AA)
cv2.line(canvas, (70, 280), (890, 280), (44, 44, 239), 2)

legacy_metrics = [
    "* REBUILD INVESTMENT LURK : $4.8 TRILLION USD",
    "* ANNUAL HEAT TRANSMISSION LOSS : 5% TO 7% RANGE",
    "* PARASITIC LINE RESISTANCE WASTE : 246 BILLION kWh/YR",
    "* ANNUAL VALUE BURNED INTO THIN AIR : $27.06 BILLION",
    "* AVERAGE POWER TRANSFORMER AGE : 40+ YEARS OLD",
    "* EMP & DIRECT LIGHTNING DEFENSE : 0.00% SHIELDING",
    "* LOAD-BALANCING CONTROL STATE : FRAGILE DIGITAL RISK"
]

y_pos = 350
for metric in legacy_metrics:
    cv2.putText(canvas, metric, (70, y_pos), font, 0.72, (200, 200, 255), 2, cv2.LINE_AA)
    y_pos += 80

# ⚡ 4. RIGHT PANEL: PROJECT RESONANT INFRASTRUCTURE PARITY
cv2.rectangle(canvas, (1000, 140), (1880, 1000), (32, 78, 14), -1)
cv2.rectangle(canvas, (1000, 140), (1880, 1000), (129, 217, 16), 2)
cv2.putText(canvas, "PROJECT RESONANT INFRASTRUCTURE", (1030, 200), font, 1.1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(canvas, "EGAIN METAMATERIAL POWER RESONANCE", (1030, 250), font, 0.9, (244, 242, 0), 2, cv2.LINE_AA)
cv2.line(canvas, (1030, 280), (1850, 280), (129, 217, 16), 2)

resonant_metrics = [
    "* CARRIER PROPAGATION FREQUENCY : 12.5 kHz TUNED",
    "* MAXIMUM HOP ATTENUATION PATH LOSS : 4.06% AT 15km",
    "* WIRELESS POWER TRANSMISSION FLOOR : 95.94% EFFICIENCY",
    "* TARGET HARDWARE RUNTIME CYCLE : 500+ YEAR OPERATIONAL LIFE",
    "* SOLID-STATE HARDENING INSULATION : 140 dB ABSOLUTE EMP CEILING",
    "* REGENERATION PURIFIER CELL POTENTIAL : +0.23V GALVANIC BIAS",
    "* LOAD-BALANCING AUTONOMOUS ROUTE : 3.82 m/s CURIE-SWITCH"
]

y_pos = 350
for metric in resonant_metrics:
    cv2.putText(canvas, metric, (1030, y_pos), font, 0.72, (230, 255, 230), 2, cv2.LINE_AA)
    y_pos += 80

# Universal Header Stamp Bar
cv2.rectangle(canvas, (0, 0), (1920, 80), (12, 10, 6), -1)
cv2.putText(canvas, "PROJECT RESONANT INFRASTRUCTURE // FINANCIAL SHOWDOWN LEDGER // SHIELD v1.0.0", (30, 50), font, 0.85, (245, 158, 11), 2, cv2.LINE_AA)

cv2.imwrite("grid88-vs-legacy-finance.png", canvas)
print("SUCCESS: Infographic 1 (Finance) generated perfectly.")
