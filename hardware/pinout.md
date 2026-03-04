\# Raspberry Pi 5 Pinout (BCM)



This project uses BCM numbering.



\## Stepper Driver (A4988 / DRV8825)

\- DIR  -> BCM 20

\- STEP -> BCM 21

\- EN   -> BCM 16 (optional, active LOW)



Power:

\- Driver VDD -> Pi 3.3V

\- Driver GND -> Pi GND

\- Motor VMOT -> external motor supply (e.g., 12V) + capacitor near driver

\- Motor GND  -> external motor ground



IMPORTANT:

\- Share a common GND between motor supply and Raspberry Pi GND.



\## Servo Gate (MG90S)

\- Signal -> BCM 18 (PWM)

\- V+     -> External 5V supply (NOT Pi 5V pin for safety)

\- GND    -> External 5V ground

\- Common GND with Pi



\## IR Break-Beam Sensor

\- Signal -> BCM 23

\- VCC    -> 3.3V or 5V (depends on module; use 3.3V if supported)

\- GND    -> Pi GND



Logic:

\- Many break-beams output LOW when beam is broken.



\## Hall Sensor (Home)

\- Signal -> BCM 24

\- VCC    -> 3.3V

\- GND    -> Pi GND



Logic:

\- Many hall modules output LOW near magnet.

