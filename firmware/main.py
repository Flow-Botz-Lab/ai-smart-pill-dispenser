from __future__ import annotations
import time

from .config import GATE_OPEN_SECONDS, DISPENSE_TIMEOUT_SEC
from .stepper import Stepper
from .servo_gate import ServoGate
from .sensors import Sensors
from .carousel import Carousel


def dispense(slot: int) -> None:
    stepper = Stepper()
    sensors = Sensors()
    gate = ServoGate()
    carousel = Carousel(stepper, sensors)

    try:
        print("Homing carousel...")
        carousel.home()
        print("Homed to slot 1.")

        print(f"Rotating to slot {slot}...")
        carousel.rotate_to_slot(slot)
        print("At target slot.")

        print("Opening gate...")
        gate.open()
        time.sleep(GATE_OPEN_SECONDS)
        gate.close()
        print("Gate closed. Waiting for pill detection...")

        detected = sensors.wait_for_ir(DISPENSE_TIMEOUT_SEC)

        if detected:
            print("✅ Dispense confirmed (IR triggered).")
        else:
            print("⚠️ No pill detected. Try micro-jog and retry once.")
            # micro-jog: small forward/back shake to dislodge
            stepper.step(20, direction=1)
            stepper.step(20, direction=-1)

            gate.open()
            time.sleep(GATE_OPEN_SECONDS)
            gate.close()

            detected2 = sensors.wait_for_ir(DISPENSE_TIMEOUT_SEC)
            if detected2:
                print("✅ Dispense confirmed after retry.")
            else:
                print("❌ Dispense failed after retry. Check jams/sensor alignment.")

    finally:
        gate.stop()
        stepper.cleanup()


if __name__ == "__main__":
    # Demo: dispense from slot 2
    dispense(slot=2)