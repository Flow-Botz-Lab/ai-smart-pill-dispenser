from __future__ import annotations
import time
import RPi.GPIO as GPIO

from .config import (
    STEPPER_DIR_PIN, STEPPER_STEP_PIN, STEPPER_EN_PIN,
    STEPPER_STEPS_PER_REV, STEPPER_MICROSTEP,
    STEP_PULSE_SEC, STEP_DELAY_SEC,
)


class Stepper:
    """
    Simple A4988/DRV8825 stepper driver controller using GPIO.

    Wiring:
      - DIR -> STEPPER_DIR_PIN
      - STEP -> STEPPER_STEP_PIN
      - EN -> STEPPER_EN_PIN (optional; active LOW for many drivers)
    """

    def __init__(self) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(STEPPER_DIR_PIN, GPIO.OUT)
        GPIO.setup(STEPPER_STEP_PIN, GPIO.OUT)

        if STEPPER_EN_PIN is not None:
            GPIO.setup(STEPPER_EN_PIN, GPIO.OUT)
            # Enable driver (active LOW)
            GPIO.output(STEPPER_EN_PIN, GPIO.LOW)

        GPIO.output(STEPPER_STEP_PIN, GPIO.LOW)

    def enable(self) -> None:
        if STEPPER_EN_PIN is not None:
            GPIO.output(STEPPER_EN_PIN, GPIO.LOW)

    def disable(self) -> None:
        if STEPPER_EN_PIN is not None:
            GPIO.output(STEPPER_EN_PIN, GPIO.HIGH)

    def step(self, steps: int, direction: int = 1) -> None:
        """
        steps: number of microsteps (already multiplied by microstep factor if desired)
        direction: 1 or -1
        """
        if direction not in (1, -1):
            raise ValueError("direction must be 1 or -1")

        GPIO.output(STEPPER_DIR_PIN, GPIO.HIGH if direction == 1 else GPIO.LOW)

        for _ in range(abs(steps)):
            GPIO.output(STEPPER_STEP_PIN, GPIO.HIGH)
            time.sleep(STEP_PULSE_SEC)
            GPIO.output(STEPPER_STEP_PIN, GPIO.LOW)
            time.sleep(STEP_DELAY_SEC)

    def steps_for_slot(self, slots: int) -> int:
        """
        Compute microsteps to rotate exactly one slot.
        """
        microsteps_per_rev = STEPPER_STEPS_PER_REV * STEPPER_MICROSTEP
        return int(microsteps_per_rev / slots)

    def cleanup(self) -> None:
        self.disable()
        GPIO.cleanup()