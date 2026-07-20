import time
import os
from gpiozero import Button
import sounddevice as sd
from scipy.io import wavfile
import numpy as np
import queue


btn_a = Button(12)
btn_b = Button(13, hold_time = 2)


sample_rate = 44100
output_dir = "recordings"
audio_frames = []
is_recording = False
audio_stream = None
finished_recordings = queue.Queue()


def audio_callback(indata, frames, time, status): # sounddevice library strictly expects callback function to have four arguments
    audio_frames.append(indata.copy())


def start_recording():
    global is_recording, audio_frames, audio_stream
    if is_recording:
        return
    is_recording = True
    audio_frames = []
    audio_stream = sd.InputStream(samplerate = sample_rate, channels=1, callback=audio_callback)
    audio_stream.start()


def stop_recording():
    global is_recording, audio_stream
    filename = None
    if not is_recording:
        return
    if audio_stream:
        audio_stream.stop()
        audio_stream.close()
        audio_stream = None
    if audio_frames:
        full_audio = np.concatenate(audio_frames, axis = 0)
        filename = os.path.join(output_dir, f"{int(time.time())}.wav")
        wavfile.write(filename, sample_rate, full_audio)
        finished_recordings.put(filename)
    is_recording = False
    return filename


def get_latest_recordings():
    try:
        return finished_recordings.get_nowait()
    except queue.Empty:
        return None


def safe_shutdown():
    print("Shutdown button held, safely powering off rpi5")
    os.system("sudo poweroff")

btn_a.when_pressed = start_recording
btn_a.when_released = stop_recording


btn_b.when_held = safe_shutdown