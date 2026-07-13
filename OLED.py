# Note: on the rpi5, do sudo apt install libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7-dev libtiff6-dev
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1106
from PIL import Image, ImageSequence # this is for gifs
import time


serial = i2c(port=1, address=0x3C)
device = ssd1106(serial, width=128, height=64)


def oled(file_path):
    img = Image.open(file_path)
    if hasattr(img, "is_animated") and img.is_animated:
        for frame in ImageSequence.Iterator(img):
            device.display(frame.convert('1'))
            time.sleep(0.1)
    else:
        device.display(img.convert('1'))