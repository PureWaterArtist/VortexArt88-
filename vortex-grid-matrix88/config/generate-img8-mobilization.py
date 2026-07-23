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
cv2.putText(canvas, "CORPORATE PATCHWORK DEPLOY", (70, 200), font, 1.1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(canvas, "X SYSTEM CRITICAL LIABILITIES", (70, 250), font, 0.9, (68, 68, 239), 2, cv2.LINE_AA)
cv2.line(canvas, (70, 280), (890, 280), (44, 44, 239), 2)

left_lines = [
    "* UTILITY INFRA STRUCTURE  : 3000+ PRIVATE ENERGY MONOPOLIES",
    "* DEPLOYMENT LAND CONFLICTS : EXPENSIVE LEGAL EASEMENT LITIGATIONS",
    "* REGIONAL HARDWARE FREQUENCIES: VARIANT DRIFT LOSSES BEYOND 12.5 kHz",
    "* INTER-STATE REAGENT HOARDING: GALLIUM RESIN MATERIAL SUPPLY BOTTLENECK",
    "* SYSTEM CUTOVER TIMELINE ROOF: 30+ YEAR FRAGILE GRID DELAY",
    "* TRANSMISSION DROP WASTE    : COAXIAL FLUXES SCATTER OUT TO SPACE",
    "* CONTINENTAL RESILIENCE GAP  : RECURRING VULNERABILITY TO DISASTER"
]
y_pos = 350
for line in left_lines:
    cv2.putText(canvas, line, (70, y_pos), font, 0.72, (200, 200, 255), 2, cv2.LINE_AA)
    y_pos += 80

# Right Panel
cv2.rectangle(canvas, (1000, 140), (1880, 1000), (32, 78, 14), -1)
cv2.rectangle(canvas, (1000, 140), (1880, 1000), (129, 217, 16), 2)
cv2.putText(canvas, "UNIFIED CIVILIZATIONAL FOCUS", (1030, 200), font, 1.1, (255, 255, 255), 3, cv2.LINE_AA)
cv2.putText(canvas, "O IMMORTAL PARITY ADVANTAGE", (1030, 250), font, 0.9, (244, 242, 0), 2, cv2.LINE_AA)
cv2.line(canvas, (1030, 280), (1850, 280), (129, 217, 16), 2)

right_lines = [
    "* UTILITY INFRA STRUCTURE  : ONE STANDARDIZED CORE SOURCE MANUAL",
    "* DEPLOYMENT COORDINATION  : PARALLEL LOCAL ENCLAVE INSTALLATIONS",
    "* FREQUENCY IMPEDANCE PARITY: ABSOLUTE ZERO DATA CODE LEVEL PARAM DRIFT",
    "* LOGISTICS MATERIAL ROUTES : DIRECT TOPOGRAPHICAL koordin COORDINATES",
    "* SYSTEM TOTAL TRANSITION ROOF: FIVE YEARS FLAT TO NATION-WIDE CUTOVER",
    "* ANNUAL ENERGY ENERGY RECLAIMED: $27.06 BILLION LINE DROP RESCUE",
    "* RECLAIMED GENERATIONAL WEALTH: $1.2 TRILLION IN AUX RE-INVESTMENT FUNDS"
]
y_pos = 350
for line in right_lines:
    cv2.putText(canvas, line, (1030, y_pos), font, 0.72, (230, 255, 230), 2, cv2.LINE_AA)
    y_pos += 80

cv2.rectangle(canvas, (0, 0), (1920, 80), (12, 10, 6), -1)
cv2.putText(canvas, "PROJECT RESONANT INFRASTRUCTURE // NATIONAL MOBILIZATION WORKFLOWS // SHIELD v1.0.0", (30, 50), font, 0.85, (245, 158, 11), 2, cv2.LINE_AA)

cv2.imwrite("grid88-vs-legacy-mobilization.png", canvas)
print("SUCCESS: Infographic 8 (Mobilization) generated perfectly.")
