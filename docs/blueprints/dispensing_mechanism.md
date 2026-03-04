\# Dispensing Mechanism Blueprint (Carousel + Gate)



\## Mechanism

Rotating pill carousel + fixed selector plate + servo sliding shutter gate.



\## Dispense Flow

1\. Reminder triggers dose time

2\. User authenticates (Face/QR/PIN)

3\. Stepper rotates carousel to correct compartment

4\. Servo opens gate (0.5–1.0s)

5\. Pills drop into chute and cup

6\. IR sensor confirms dispense

7\. Log event locally + upload to cloud



\## Core Parts

\- Carousel: Ø110mm, 8 slots, walls 20–22mm

\- Selector plate: Ø115mm, 4mm thick, drop hole Ø16mm with 45° chamfer

\- Stepper: NEMA 17 + A4988/DRV8825

\- Gate: MG90S servo + sliding shutter (20mm travel)

\- Sensors: IR break beam (drop), Hall + magnet (home)



\## Anti-Jam Features

\- 5–10° sloped compartment floor toward exit

\- 1–2mm fillets on interior corners

\- Funnel chamfer into drop hole

\- “Micro-jog” retry routine if no pill detected



\## Child Safety

\- Shutter defaults closed

\- Only 1 exit hole

\- Dispense requires authentication

