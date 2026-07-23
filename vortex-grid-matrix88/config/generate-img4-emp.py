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
cv2.putText(canvas, "LEGACY HIGH-VOLTAGE NETWORKS", (70, 200), font, 1.1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(canvas, "X SYSTEM CRITICAL LIABILITIES", (70, 250), font, 0.9, (68, 68, 239), 2, cv2.LINE_AA)
cv2.line(canvas, (70, 280), (890, 280), (44, 44, 239), 2)

left_lines = [
    "* GRID ELECTROMAGNETIC PROX: SEVERE LONG WIRE ANTENNAS",
    "* SURGE INDUCTION PROFILE  : CATASTROPHIC CURRENT RAMP",
    "* MULTI-TON TRANSFORMER EXP: INSTANT SILICON TRANS MELTDOWN",
    "* HIGH-ALTITUDE EMP RESIST : 0% SHIELD PROTECTION RATIO",
    "* SOLAR CME STORM RESILIENCE: TOTAL CORE SYSTEM BREAKDOWN",
    "* HARDWARE RE-SOURCING LEAD : 2+ YEAR FOUNDRY FOUNDATION DELAY",
    "* BLACKOUT CASCADE DURATION : YEARS OF TOTAL CRITICAL FREEZE"
]
y_pos = 350
for line in left_lines:
    cv2.putText(canvas, line, (70, y_pos), font, 0.72, (200, 200, 255), 2, cv2.LINE_AA)
    y_pos += 80

# Right Panel
cv2.rectangle(canvas, (1000, 140), (1880, 1000), (32, 78, 14), -1)
cv2.rectangle(canvas, (1000, 140), (1880, 1000), (129, 217, 16), 2)
cv2.putText(canvas, "RESONANT HARMONIC SHIELDING", (1030, 200), font, 1.1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(canvas, "O IMMORTAL PARITY ADVANTAGE", (1030, 250), font, 0.9, (244, 242, 0), 2, cv2.LINE_AA)
cv2.line(canvas, (1030, 280), (1850, 280), (129, 217, 16), 2)

right_lines = [
    "* GRID ELECTROMAGNETIC PROX: NON-METALLIC ISOLATED TOWERS",
    "* SURGE INDUCTION PROFILE  : ZERO COUPLING WIRE TRACKS",
    "* EXTERIOR HOUSING MATERIAL: ULTRA-HIGH STIFFNESS POLYMER",
    "* RE-RE-ARC PULSE ATTENUATION : 140 dB ABSOLUTE EMP SHIELD",
    "* LIGHTNING CLOUD HIT IMPACT: 100% INSTANT GROUND BED DISSIPATION",
    "* CORE CHANNEL SURGE LEAKAGE: 0.00% COMPLETE ISOLATION PROOFS",
    "* NETWORK SURVIVAL PROFILE : ZERO DRIFT CONTINUOUS GRID SERVICE"
]
y_pos = 350
for line in right_lines:
    cv2.putText(canvas, line, (1030, y_pos), font, 0.72, (230, 255, 230), 2, cv2.LINE_AA)
    y_pos += 80

cv2.rectangle(canvas, (0, 0), (1920, 80), (12, 10, 6), -1)
cv2.putText(canvas, "PROJECT RESONANT INFRASTRUCTURE // EMP BLAST SHOCK ISOLATION // SHIELD v1.0.0", (30, 50), font, 0.85, (245, 158, 11), 2, cv2.LINE_AA)

cv2.imwrite("grid88-vs-legacy-emp.png", canvas)
print("SUCCESS: Infographic 4 (EMP Shield) generated perfectly.")
