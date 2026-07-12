# Note: on the rpi5, do sudo apt install libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7-dev libtiff6-dev
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1106
from PIL import Image
import time

serial = i2c(port=1, adress=0x3C)
device = ssd1106(serial, width=128, height=64)

def oled(file_path):
    img = Image.open(file_path).convert('1')
    device.display(img)
    time.sleep(10)