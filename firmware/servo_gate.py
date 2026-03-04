from __future__ import annotations
import time

import pigpio

from .config import SERVO_PIN, SERVO_CLOSED_US, SERVO_OPEN_US


class ServoGate:
    """
    Gate servo controlled via pigpio for stable PWM on Raspberry Pi.
    """

    def __init__(self) -> None:
        self.pi = pigpio.pi()
        if not self.pi.connected:
            raise RuntimeError("pigpio daemon not running. Run: sudo systemctl enable --now pigpiod")

        # Set to closed on startup
        self.close()

    def open(self) -> None:
        self.pi.set_servo_pulsewidth(SERVO_PIN, SERVO_OPEN_US)

    def close(self) -> None:
        self.pi.set_servo_pulsewidth(SERVO_PIN, SERVO_CLOSED_US)

    def pulse_open(self, seconds: float) -> None:
        self.open()
        time.sleep(seconds)
        self.close()

    def stop(self) -> None:
        # Stop PWM
        self.pi.set_servo_pulsewidth(SERVO_PIN, 0)
        self.pi.stop()