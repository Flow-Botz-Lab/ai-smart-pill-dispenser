\# Wiring Guide (Quick)



\## Common Rule

All grounds must be shared:

\- Pi GND

\- Stepper driver GND

\- Servo power GND

\- Sensor GND



\## Recommended Power

\- Raspberry Pi 5: stable 5V (USB-C PSU or buck converter)

\- Stepper motor: separate supply (e.g., 12V for NEMA 17)

\- Servo: separate 5V rail (buck converter), not from Pi 5V pin



\## Connections Summary

Stepper:

\- Pi BCM20 -> A4988 DIR

\- Pi BCM21 -> A4988 STEP

\- Pi BCM16 -> A4988 EN (optional)



Servo:

\- Pi BCM18 -> Servo signal

\- External 5V -> Servo V+

\- GND shared



Sensors:

\- Pi BCM23 -> IR break-beam signal

\- Pi BCM24 -> Hall sensor signal

