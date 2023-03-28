import RPi.GPIO as GPIO


class Valve():

    def __init__(self, pin):
        self.pin = pin

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def init(self):
        GPIO.setup(self.pin, GPIO.OUT)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)


class ValveManager:
    is_init = False

    @staticmethod
    def LEFT():
        return Valve(24)

    @staticmethod
    def RIGHT():
        return Valve(23)

    @staticmethod
    def BASE():
        return Valve(22)

    @staticmethod
    def init():
        if (ValveManager.is_init):
            return
        GPIO.setmode(GPIO.BCM)
        pins = [ValveManager.LEFT(), ValveManager.RIGHT(), ValveManager.BASE()]
        for pin in pins:
            pin.init()
        ValveManager.is_init = True
