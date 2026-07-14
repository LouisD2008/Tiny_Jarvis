from piper import PiperVoice
import pyaudio  # basically a python wrapper for the C library portaudio


voice = PiperVoice.load("piper_voices/en_US-lessac-medium.onnx")
p = pyaudio.PyAudio()


# Note : download a voice with `python -m piper.download_voices en_US-lessac-medium`


def speak(text):
    stream = None
    try:
        stream = p.open(
            format = pyaudio.paInt16,
            channels = 1,
            rate = voice.config.sample_rate,
            output = True
        )
        for sentence in text:
            if not sentence.strip():
                continue
            for audio_bytes in voice.synthesize_stream(sentence):
                stream.write(audio_bytes)
        return True
    except Exception as e:
        print(f"Speaker error: {e}")
        return False
    finally:
        if stream:
            stream.stop_stream()
            stream.close()