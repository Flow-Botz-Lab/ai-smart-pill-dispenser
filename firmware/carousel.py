from __future__ import annotations
import time

from .config import CAROUSEL_SLOTS, HOME_SEARCH_DIR
from .stepper import Stepper
from .sensors import Sensors


class Carousel:
    """
    Carousel logic:
    - Home using hall sensor + magnet under Slot 1
    - Rotate exact slot-to-slot steps
    """

    def __init__(self, stepper: Stepper, sensors: Sensors) -> None:
        self.stepper = stepper
        self.sensors = sensors
        self.slot_steps = self.stepper.steps_for_slot(CAROUSEL_SLOTS)
        self.current_slot = None  # unknown until homed

    def home(self, max_revs: float = 2.0) -> None:
        """
        Rotate until hall sensor is triggered (slot 1).
        """
        # If already on magnet, move slightly away first
        if self.sensors.hall_triggered():
            self.stepper.step(int(self.slot_steps * 0.25), direction=HOME_SEARCH_DIR)

        max_steps = int(self.slot_steps * CAROUSEL_SLOTS * max_revs)
        moved = 0

        while moved < max_steps:
            if self.sensors.hall_triggered():
                self.current_slot = 1
                return
            self.stepper.step(5, direction=HOME_SEARCH_DIR)  # small increments for accurate trigger
            moved += 5
            time.sleep(0.002)

        raise RuntimeError("Home not found: hall sensor never triggered. Check wiring/magnet placement.")

    def rotate_to_slot(self, target_slot: int) -> None:
        if not (1 <= target_slot <= CAROUSEL_SLOTS):
            raise ValueError(f"target_slot must be 1..{CAROUSEL_SLOTS}")

        if self.current_slot is None:
            raise RuntimeError("Carousel not homed. Call home() first.")

        delta = target_slot - self.current_slot
        if delta < 0:
            delta += CAROUSEL_SLOTS

        steps = delta * self.slot_steps
        if steps:
            self.stepper.step(steps, direction=HOME_SEARCH_DIR)

        self.current_slot = target_slot