# Note: on the rpi5, do sudo apt install libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7-dev libtiff6-dev
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1106
from PIL import Image, ImageSequence # this is for gifs
import time
import threading


serial = i2c(port=1, address=0x3C)
device = ssd1106(serial, width=128, height=64)


def oled(file_path, stop_event=None):   # stop_event is the thread signal here
    img = Image.open(file_path)
    if hasattr(img, "is_animated") and img.is_animated:
        while stop_event is None or not stop_event.is_set():
            for frame in ImageSequence.Iterator(img):
                if stop_event and stop_event.is_set():
                    break
                device.display(frame.convert('1'))
                time.sleep(0.1)
    else:
        device.display(img.convert('1'))


class AssistantDisplay:
    def __init__(self):
        self.switch = threading.Event()
        self.thread = None
    def show(self, file_path):
        self.stop()
        self.switch.clear()
        self.thread = threading.Thread(target = oled, args=(file_path, self.switch))
        self.thread.start()
    def stop(self):
        self.switch.set()
        if self.thread and self.thread.is_alive():
            self.thread.join()
