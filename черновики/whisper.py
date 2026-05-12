import черновики.whisper as whisper

# 1. Распознаём через Whisper
model = whisper.load_model("base")
result = model.transcribe("audio.wav", language="ru")
raw_text = result["text"]

# 2. Сохраняем как есть (уже с базовой пунктуацией)
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(raw_text)

print("✅ Готово! Текст сохранён")

# 3. Для красивого оформления нужно либо:
# а) Вручную добавить заголовки и структуру
# б) Использовать второй ИИ (GPT/RuT5)
# в) Использовать шаблоны Markdown