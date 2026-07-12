from faster_whisper import WhisperModel


def transcribe_audio(file):
    model = WhisperModel("tiny", device="cpu", compute_type="int8")
    segments, info = model.transcribe(file, beam_size = 5)
    transcription = ""
    for segment in segments:
        transcription = transcription + segment.text
    return transcription.strip()