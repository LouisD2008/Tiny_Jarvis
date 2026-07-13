import listener # This will initialize listener.py once
from speaker import speak
from transcriber import transcribe_audio
from OLED import oled
from ai import generate
import glob
import os
import time


def get_latest_recordings():
    wav_files = glob.glob(os.path.join("recordings", "*.wav"))
    if not wav_files:
        return None
    return sorted(wav_files)[0]


def main():
    print("Tiny Jarvis is active and listening!")
    oled("home.png")
    while True:
        audio_file = get_latest_recordings()
        if audio_file:
            try:
                print(f"Found new recording: {audio_file}")
                print("Transcribing audio...")
                prompt = transcribe_audio(audio_file)
                print(f"Prompt : {prompt}")
                if not prompt.strip():
                    print("Empty transcription. Skipping.")
                    os.remove(audio_file)
                    continue # skips the rest of the code in this iteration and goes back to the top of the while loop
                print("Generating response...")
                oled("thinking_animation.gif")
                ai_response = generate(prompt)
                print(f"Jarvis: {ai_response}")
                print("Generating speech...")
                speech_success = speak(ai_response)
                if speech_success:
                    print("Success! playing response...")
                    os.system("aplay output.wav")
                else:
                    print("[ERROR] Failed to generate speech")
            except Exception as e:
                print(f"[ERROR IN PIPELINE]: {e} ")
            finally:
                if os.path.exists(audio_file):
                    os.remove(audio_file)
                    print("Deleted recording file")
        time.sleep(0.2)


if __name__ == "__main__":
    main()