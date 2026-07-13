# TINY JARVIS

## Table of contents:

 - [Description](#description)
    - [Quick description](#quick-description)
    - [Project structure](#project-structure)
    - [Application and user scenario](#application-and-user-scenario)
 - [How to install](#how-to-install)
    - [Prerequisites](#prerequisites)
    - [Dependencies](#dependencies)
    - [Other](#other)
 - [Hardware](#hardware)

# Description

## Quick description

Tiny Jarvis is a local, offline voice-controlled AI Agent that runs directly on your [Raspberry pi 5](https://www.raspberrypi.com/).\
The software for Tiny Jarvis is all in this repository, and you can take a look at the hardware [here](#hardware).

> Note: this project is still in heavy development. As such I would not recommend installing it just yet. 

## Project structure
```
Tiny_Jarvis/
├── .venv/  # virtual env with all dependencies installed
├── piper_voices/
├── recordings/
├── assets/
├── ai.py
├── listener.py
├── main.py  # the main script
├── OLED.py
├── speaker.py
├── transcriber.py
├── README.md
└── requirements.txt
```
## Application and User Scenario

The OLED screen shows an `IDLE` animation when idle.\
User presses a button, gives a command, and releases the button when done speaking.\
The captured audio is translated into text by [faster-whisper](https://pypi.org/project/faster-whisper/0.3.0/).
That text is given as a prompt to a model of your choice using [Ollama](https://ollama.com/), preferably a low-parameter model like Qwen3-0.6B, balancing speed and quality.\
The model's ouput is streamed into [Piper TTS](https://github.com/rhasspy/piper), a text-to-speech model, and played through the speakers (stereo sound).\
OLED screen shows `THINKING` and `SPEAKING` animations meanwhile.
The other button serves a single purpose: to turn off the Raspberry Pi 5 safely through `sudo poweroff`.

If the user's prompt starts with "Play ...", then the prompt is rerouted through [librespot](https://github.com/librespot-org/librespot) to play some music using Spotify premium! 
> Note: This only works when connected to Wifi. Also this is still in development.


# How to install

## Prerequisites
Before doing anything, create a .venv and install python (system-wide).
Run these commands:

```bash
sudo apt update
sudo apt install python3 python3-venv
```
then in the project directory:
```bash
python3 -m venv .venv
source .venv/bin/activate   # enter the .venv
```

## Dependencies

All needed dependencies are listed in `requirements.txt`, and can be downloaded by running either commands in the root directory (in the .venv):
```bash
pip install -r requirements.txt
```
or :
```bash
pip install piper-tts luma.oled Pillow faster-whisper ollama gpiozero sounddevice scipy numpy
```

## Other

For `luma.oled`, other system-wide packages are needed.
Do 
```bash
sudo apt install libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7-dev libtiff6-dev
``` 
and for `sounddevice`:
```bash
sudo apt install libportaudio2 portaudio19-dev
```
For ollama: you need to pull a model first. For example:
```bash
ollama pull qwen3:0.6b
```
Also, the buttons need to be on the right GPIO pins.\
Button for talking should be on GPIO 17 and the other on GPIO 27, but you can change these numbers in `listener.py`.

Finally: make sure to turn on I2C in raspberry pi settings.\
Access these settings via:
```bash
sudo raspi-config
```
I2C Interface --> ON

# Hardware

Gerber files are here: COMING SOON, first PCBs are a failure and as such schematics need updating.\
same for other files needed for PCB manufacturing