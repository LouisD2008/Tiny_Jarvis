from piper import PiperVoice
import wave


voice = PiperVoice.load("piper_voices/en_US-lessac-medium.onnx")


# Note : download a voice with python -m piper.download_voices en_US-lessac-medium


def speak(text):
    try:
      with wave.open("output.wav", "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)
      return True
    except:
       return False


# Next step: streaming the audio data in chunks instead of synthetizing the entire text at once
# Look at piper documentation, its not that difficult