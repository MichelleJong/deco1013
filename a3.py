from microbit import *
import neopixel
import music
from random import randint
#from gesture import *

# libraries
#gesture = Gesture()

np = neopixel.NeoPixel(pin1, 10)

#Initial
display.show(Image.ARROW_W)
#Timer portion - Gesture - swipe left to start timer
#After timer starts the display changes to happy face
#Half of the time over -> Sad face
num_leds = 10
for i in range(num_leds):
    np[i] = (0, 255, 0)
np.show()

while True:
    for i in range(num_leds):
        np[i] = (255, 0, 0)
        np.show()
        sleep(1000)

#Music should play after the LEDs cycle once?
#How to end loop??
    if i == 10:
        np.clear()
        music.play(music.RINGTONE)
        music.stop()

#If task completed successfully (A button):
music.play(music.POWER_UP)

while True:
    for pixel_id in range(0, len(np)):
        red = randint(40, 100)
        green = randint(100, 255)
        blue = randint(0, 40)

        np[pixel_id] = (red, green, blue)

        np.show()
        sleep(50)

#If task completed unsuccessfully (B Button):
    music.play(music.POWER_DOWN)

while True:
    for pixel_id in range(0, len(np)):
        red = randint(100, 255)
        green = randint(0, 40)
        blue = randint(0, 40)

        np[pixel_id] = (red, green, blue)

        np.show()
        sleep(50)



