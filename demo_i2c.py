import machine, ssd1306, time
from machine import Pin, I2C
from time import sleep

# i2c = I2C(scl=Pin(22), sda=Pin(21))     # software I2C, none or -1
i2c = I2C(1, scl=Pin(22), sda=Pin(21))    # hardware I2C, 0 or 1
# i2c = I2C(0) # doesn't work

# you cannot use Japanese with Pymakr plugin

oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    oled.fill(0)
    oled.text('  MicroPython  ', 0, 0)
    oled.text(' on esp32 board', 0, 8)
    oled.text(' 128 x 64 OLED ', 0, 16)
    oled.text('SSD1306 Display', 0, 24)
    oled.show()

    sleep(2.0)

    oled.fill(0)
    oled.text('  MicroPython  ', 0, 0)
    oled.text('  MicroPython  ', 0, 8)
    oled.text(' on esp32 board', 0, 16)
    oled.text(' 128 x 64 OLED ', 0, 24)
    oled.text('SSD1306 Display', 0, 32)
    oled.show()

    sleep(2.0)

    oled.fill(0)
    oled.text('1234567890123456', 0, 8 * 0)
    oled.text('abcdefghijklmnop', 0, 8 * 1)
    oled.text('qrstuvwxyz-=_+{}', 0, 8 * 2)
    oled.text('~!@#$%^&*()<>?/:', 0, 8 * 3)
    oled.text('1234567890123456', 0, 8 * 4)
    oled.text('abcdefghijklmnop', 0, 8 * 5)
    oled.text('qrstuvwxyz-=_+{}', 0, 8 * 6)
    oled.text('~!@#$%^&*()<>?/:', 0, 8 * 7)
    oled.show()

    sleep(2.0)

    oled.fill(0)
    oled.text('ABCDEFGHIJKLMNOP', 0, 0)
    oled.text('QRSTUVWXYZ`~!@#$', 0, 8)
    oled.text('%^&*()_+-={}[]|\\', 0, 16)
    oled.text('<>,./?;:\'\"', 0, 24)
    oled.show()

    sleep(2.0)
