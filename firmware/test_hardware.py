"""
Hardware test script for Smart Pill Dispenser.

Tests:
1. Stepper motor rotation
2. Servo gate open/close
3. IR beam sensor
4. Hall sensor

Run this BEFORE running the full system.
"""

import time

from stepper import Stepper
from servo_gate import ServoGate
from sensors import Sensors


def test_stepper():
    print("Testing stepper motor...")

    stepper = Stepper()

    print("Forward...")
    stepper.step(400, direction=1)

    time.sleep(1)

    print("Reverse...")
    stepper.step(400, direction=-1)

    stepper.cleanup()

    print("Stepper test complete\n")


def test_servo():
    print("Testing servo gate...")

    gate = ServoGate()

    print("Opening gate...")
    gate.open()

    time.sleep(2)

    print("Closing gate...")
    gate.close()

    time.sleep(1)

    gate.stop()

    print("Servo test complete\n")


def test_sensors():
    print("Testing sensors (press Ctrl+C to stop)\n")

    sensors = Sensors()

    try:
        while True:

            if sensors.ir_triggered():
                print("IR beam broken")

            if sensors.hall_triggered():
                print("Hall sensor triggered")

            time.sleep(0.2)

    except KeyboardInterrupt:
        print("\nSensor test stopped")


if __name__ == "__main__":

    test_stepper()

    test_servo()

    test_sensors()