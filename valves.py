import RPi.GPIO as GPIO
from time import sleep

class Valve():

    def __init__(self, pin):
        self.pin = pin

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def init(self):
        GPIO.setup(self.pin, GPIO.OUT)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def toggle_state(self,state):
        GPIO.output(self.pin, GPIO.LOW if state else GPIO.HIGH)
        


class ValveManager:
    
    @staticmethod
    def run(valve,state,delay):
        ValveManager.init()
        valve_map = {
        1: ValveManager.LEFT(),
        2: ValveManager.RIGHT(),
        3: ValveManager.BASE(),
        }
        
        valve_map[valve].toggle_state(state)
        sleep(delay)

    is_init = False
    @staticmethod
    def all_off():
        pins = [ValveManager.LEFT(), ValveManager.RIGHT(),ValveManager.BASE()]
        for pin in pins: pin.off()
    def all_on(): 
        pins = [ValveManager.LEFT(), ValveManager.RIGHT(), ValveManager.BASE()]
        for pin in pins: pin.on()

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
