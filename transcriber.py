from faster_whisper import WhisperModel
model = WhisperModel("tiny", device="cpu", compute_type="int8")


def transcribe_audio(file):
    segments, info = model.transcribe(file, beam_size = 5)
    transcription = ""
    for segment in segments:
        transcription = transcription + segment.text
    return transcription.strip()