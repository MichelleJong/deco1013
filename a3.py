from microbit import *
from gesture import *
import neopixel
from random import randint
import music
gesture_sensor = Gesture()
np = neopixel.NeoPixel(pin1, 10)

display.show(Image.ARROW_S)
num_leds = 10
for i in range(num_leds):
    np[i] = (0, 255, 0)
np.show()

while True:
    g = gesture_sensor.read()

    if g == 'down':
        display.show(Image.SMILE)
        for i in range(num_leds):
            np[i] = (255, 0, 0)
            sleep(1000)
            np.show()
            if i == 10:
                music.play(music.RINGTONE)

    elif g == 'up':
        for i in range(num_leds):
            np[i] = (0, 255, 0)
            np.show()
    sleep(100)
    
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        music.play(music.POWER_UP)
        for i in range(num_leds):
            red = randint(40, 100)
            green = randint(100, 255)
            blue = randint(0, 40)
            np[i] = (red, green, blue)

        np.show()
        sleep(50)

    if button_b.is_pressed():
        display.show(Image.SAD)
        music.play(music.POWER_DOWN)
        for i in range(num_leds):
            red = randint(100, 255)
            green = randint(0, 40)
            blue = randint(0, 40)
            np[i] = (red, green, blue)

        np.show()
        sleep(50)



