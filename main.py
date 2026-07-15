import listener # This will initialize listener.py once
from speaker import speak
from transcriber import transcribe_audio
from OLED import AssistantDisplay
from ai import generate, sentence_buffer
import os
import time


def main():
    d = AssistantDisplay()
    if not os.path.exists("recordings"):  # small check in case recordings/ dir doesnt exist, you never know
        print("Warning: you didn't have a recordings/ folder. Please restart the script for everything to work well.")
        os.makedirs("recordings")
    print("Tiny Jarvis is active and listening!")
    d.show("home.png")
    while True:
        audio_file = listener.get_latest_recordings()
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
                d.show("thinking_animation.gif")
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
                    d.show("home.png")
        time.sleep(0.2)  # wait a bit in between calling get_latest_recordings()


if __name__ == "__main__":
    main()