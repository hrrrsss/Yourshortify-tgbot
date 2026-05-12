import whisper

def ai_translate():
    # 1. Распознаём через Whisper
    model = whisper.load_model("base")
    result = model.transcribe("bot/files/audio.mp3", language="ru")
    raw_text = result["text"]

    # 2. Сохраняем как есть (уже с базовой пунктуацией)
    with open("bot/files/transcript.txt", "w", encoding="utf-8") as f:
        f.write(raw_text)
    return "Nice"