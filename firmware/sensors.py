from __future__ import annotations
import time
import RPi.GPIO as GPIO

from .config import IR_BEAM_PIN, HALL_SENSOR_PIN, IR_ACTIVE_WHEN_LOW, HALL_ACTIVE_WHEN_LOW


class Sensors:
    """
    IR break-beam + Hall sensor inputs.
    Uses pull-ups by default (common for these modules).
    """

    def __init__(self) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(IR_BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(HALL_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def _active(self, pin: int, active_when_low: bool) -> bool:
        level = GPIO.input(pin)
        return (level == GPIO.LOW) if active_when_low else (level == GPIO.HIGH)

    def ir_triggered(self) -> bool:
        return self._active(IR_BEAM_PIN, IR_ACTIVE_WHEN_LOW)

    def hall_triggered(self) -> bool:
        return self._active(HALL_SENSOR_PIN, HALL_ACTIVE_WHEN_LOW)

    def wait_for_ir(self, timeout_sec: float) -> bool:
        """
        Wait until pill passes beam (triggered) within timeout.
        Returns True if triggered, False if timeout.
        """
        start = time.time()
        while time.time() - start < timeout_sec:
            if self.ir_triggered():
                return True
            time.sleep(0.01)
        return False