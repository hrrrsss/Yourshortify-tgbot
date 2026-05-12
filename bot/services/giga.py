import requests

from config.config import settings

def giga_text():
    # 1. Токен с сайта gigachat.dev
    ACCESS_TOKEN=settings.gigachat_token
    # 2. Читаем текст
    with open("bot/files/transcript.txt", "r", encoding="utf-8") as f:
        text = f.read()[:1500]

    # 3. Запрос к GigaChat
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "GigaChat",
        "messages": [
            {"role": "user", "content": f"Сделай структурированный конспект этого текста:\n\n{text}"}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }

    print("🤖 Запрашиваю конспект...")
    response = requests.post(url, headers=headers, json=data, verify=False)

    # 4. Сохраняем результат
    if response.status_code == 200:
        result = response.json()['choices'][0]['message']['content']
        
        with open("bot/files/giga.txt", "w", encoding="utf-8") as f:
            f.write(result)
        
        print(f"✅ Конспект сохранён в файл 'giga.txt'")
        print(f"📏 Размер: {len(result.split())} слов")
        
        # Показываем первые 300 символов
        print("\n📝 Первые 300 символов:")
        print("=" * 50)
        print(result[:300] + "...")
        print("=" * 50)

        with open("bot/files/giga.txt", "r", encoding="utf-8") as f:
            return f.read()
        
    else:
        print(f"❌ Ошибка {response.status_code}: {response.text}")

    return "Text is ready"