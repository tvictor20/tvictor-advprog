import time
import RPi.GPIO as GPIO
from flask import Flask, render_template

# GPIO and Sensors ============================================================

# Objects to represent sensors used to get water level
class WaterLevelSensor:

    # how high the sensor is above the top of the fish tank
    offset = 0

    def __init__(self, echo, trig):
        self.echo_pin = echo
        self.trig_pin = trig
        GPIO.setup(self.trig_pin, GPIO.OUT, initial=0)
        GPIO.setup(self.echo_pin, GPIO.IN)

    # gets the time it took for the sound to return, in microseconds
    def pulse_in(self):
        GPIO.output(self.trig_pin, 1)
        time.sleep(0.05)
        GPIO.output(self.trig_pin, 0)
        start = time.clock()
        GPIO.wait_for_edge(self.echo_pin, GPIO.RISING)
        return time.clock() - start

    # returns how far away the water is from the top of the tank in centimeters
    def read_water_level(self):
        # the speed of sound is ~343 m/s
        val = self.pulse_in() * 0.000001715 # ((1 / 1,000,000) * 343) / 2,000
        return val - ofset

# Webpage =====================================================================
app = Flask(__name__)

# Posts new readings to the webpage
@route('/')
def display_info():
    reading = 0
    render_template('info.html', height=reading)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    app.run('127.0.0.1', 8000)
