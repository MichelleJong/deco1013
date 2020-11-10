from microbit import *
import neopixel
import music
from random import randint
##from gesture import *

# libraries
#gesture = Gesture()

np = neopixel.NeoPixel(pin1, 10)

num_leds = 10
for i in range(num_leds):
    np[i] = (0, 255, 0)
np.show()

while True:
    for i in range(num_leds):
        np[i] = (255, 0, 0)
        np.show()
        sleep(500)
#Music should play after the LEDs cycle once?
    if i == 10:
        np.clear()
        music.play(music.RINGTONE)
        music.stop()




