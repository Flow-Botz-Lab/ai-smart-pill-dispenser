"""
Hardware pin config for Raspberry Pi 5.
Edit these pins to match your wiring.

NOTE:
- Stepper uses A4988/DRV8825: DIR, STEP, EN
- Servo uses pigpio (stable PWM)
- IR break-beam uses GPIO input with pull-up
- Hall sensor uses GPIO input with pull-up
"""

# -----------------------------
# STEPPER (A4988 / DRV8825)
# -----------------------------
STEPPER_DIR_PIN = 20
STEPPER_STEP_PIN = 21
STEPPER_EN_PIN = 16  # active LOW for many drivers

# Microstepping pins (optional, if you wire them)
# If not wired, driver defaults to full step.
STEPPER_MS1_PIN = None
STEPPER_MS2_PIN = None
STEPPER_MS3_PIN = None

# Steps per revolution for your motor:
# - Typical NEMA17 = 200 full steps/rev (1.8°)
STEPPER_STEPS_PER_REV = 200

# Microstepping factor (1, 2, 4, 8, 16, 32)
STEPPER_MICROSTEP = 16

# Carousel slots
CAROUSEL_SLOTS = 8  # set 8 or 12
HOME_SEARCH_DIR = 1  # 1 = one direction, -1 = other direction

# -----------------------------
# SERVO (Gate)
# -----------------------------
SERVO_PIN = 18  # PWM-capable pin
SERVO_CLOSED_US = 1100  # microseconds (tune)
SERVO_OPEN_US = 1700    # microseconds (tune)

# -----------------------------
# SENSORS
# -----------------------------
IR_BEAM_PIN = 23    # break-beam receiver output
HALL_SENSOR_PIN = 24

# True/False depending on your sensor logic.
# Many break-beams output LOW when beam is broken.
IR_ACTIVE_WHEN_LOW = True
HALL_ACTIVE_WHEN_LOW = True

# -----------------------------
# TIMING
# -----------------------------
STEP_PULSE_SEC = 0.0008  # 800 µs (tune for reliable motion)
STEP_DELAY_SEC = 0.0008  # delay between pulses
GATE_OPEN_SECONDS = 0.8  # how long to hold gate open
DISPENSE_TIMEOUT_SEC = 2.0  # time to wait for pill detection