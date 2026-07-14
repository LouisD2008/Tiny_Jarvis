import listener # This will initialize listener.py once
from speaker import speak
from transcriber import transcribe_audio
from OLED import oled
from ai import generate
import glob   # some sort of regex, basically for finding file path names that follow a specific pattern
import os
import time
import threading


def get_latest_recordings():
    wav_files = glob.glob(os.path.join("recordings", "*.wav"))
    if not wav_files:
        return None
    return sorted(wav_files)[0]


def sentence_buffer(token_gen):
    buffer = ""
    sentence_endings = {'.', '?', '!', '\n', ';', ':'}
    for token in token_gen:
        buffer += token
        if any(buffer.strip().endswith(ending) for ending in sentence_endings):  # any keyword returns True if any item in an iterable is True, so here if any buffer element ends with one of the elements in sentence_endings
            yield buffer.strip()
            buffer = ""
    if buffer.strip():
        yield buffer.strip()


def main():
    if not os.path.exists("recordings"):  # small check in case recordings/ dir doesnt exist, you never know
        print("Warning: you didn't have a recordings/ folder. Please restart the script for everything to work well.")
        os.makedirs("recordings")
    print("Tiny Jarvis is active and listening!")
    switch = threading.Event()   # starts as False
    idle_anim_thread = threading.Thread(target=oled, args=("home.png", switch))   # creates the idle animation thread
    idle_anim_thread.start()   # starts the idle animation thread (it will actually finish instantly since its just a png)
    while True:
        thinking_anim_thread = None
        audio_file = get_latest_recordings()
        if audio_file:  # if audio recordings are found in recordings/
            try:
                print(f"Found new recording: {audio_file}")
                print("Transcribing audio...")
                prompt = transcribe_audio(audio_file)  # fast-whisper at work turning that .wav file into text
                print(f"Prompt : {prompt}")
                if not prompt.strip():  # if the user didn't say anything, if faster-whisper returned nothing
                    print("Empty transcription. Skipping.")
                    os.remove(audio_file)
                    continue # skips the rest of the code in this iteration and goes back to the top of the while loop
                print("Generating response...")
                switch.set()  # the switch is set to True, the function in OLED.py finishes bc of the while loop
                idle_anim_thread.join()  # we wait for that thread to finish and kill it
                switch.clear()  # we reset the switch to False
                thinking_anim_thread = threading.Thread(target=oled, args=("thinking_animation.gif", switch))  # we create another thread for the thinking animation
                thinking_anim_thread.start()  # starts the thinking animation thread
                raw_token_stream = generate(prompt)  # the raw token stream generated in real time by the ai chatbot
                sentence_stream = sentence_buffer(raw_token_stream)  # we "filter" that raw token stream into a list of sentences
                speech_success = speak(sentence_stream)  # that list/stream of sentences is poured into the speakers!
                if not speech_success:
                    print("Failed to stream speech")
            except Exception as e:  # to catch any errors at any time in the process
                print(f"[ERROR IN PIPELINE]: {e} ")
            finally:  # whether the "try" or "except" blocks was executed, this will run in the "if audio_file" block
                if os.path.exists(audio_file):
                    os.remove(audio_file)
                    print("Deleted recording file")
                    switch.set()  # set the switch to true, signaling the gif to stop playing in OLED.py
                    if thinking_anim_thread is not None:
                        thinking_anim_thread.join()   # we wait for that thread to finish them kill it
                    switch.clear()  # reset the switch back to False
                    idle_anim_thread = threading.Thread(target=oled, args=("home.png", switch))   # we create a new thread for idle png, bc once you killed a thread, you can't revive it, you have to declare it all over again
                    idle_anim_thread.start()  # starts the idle png thread
        time.sleep(0.2)  # wait a bit in between calling get_latest_recordings()


if __name__ == "__main__":
    main()