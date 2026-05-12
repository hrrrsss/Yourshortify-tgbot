import requests

def giga_text():
    # 1. Токен с сайта gigachat.dev
    ACCESS_TOKEN="eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.h0Ki8eLd5wq0PtCzIsyR212qTWG5tuJVknsM10Gog0oTSFCvKXfSCgKWQDvH28tcDOqu9-hCfmpY_CtTibiPclCQfh7IHqpcOxOMrQxEvbU3nf5z9fVPkuPBxq58Mp8l3uE1v6eZIvzmX-7TZaRalei71vC1yZgFt9d7Ck4eQGfhLwRogpmZOcXo-XDjH8kLkhEcqNxQCLuMliOOy_MsWMNrmQti2qrVOqMfY0BUdMAl0buRhoOnpsB0yXFMJKtRtEh8rh7N1gMvv6Mb5LxaQZ6qyVd7jMa-I9acQoxXFduigf_ImBIhJO5aNwGWZqAQYLnsNZnPnKmYzXO0iVvccw.C2nC6SOkyedwj-mPB_jDaw.ZO843ImB1U6gxgJMt44LsqZYXNbDZWthyMuQLcNdKzChpxbR0CNuyfeQiDj7KM4jkE8xVYrjMntKE5f5URN9mYLUmn3Q0T1zfp5pDdo6g5jWEyDB19Ya6ac75GUWDljlh59Qg9Jq2r87xy_E8a_27bT7bFLHLbfpPAnXK0PGa66nenDRYe0ETuoBMDK0n0w3W8999dOmqytTgD7HBRRs8qFk-dFyZ0Q_xxBCPKIEUE84WT1CqoAbCwmSUGFHb44916etylDqKJrMO6CV_EgbXomHjmY57w1OdhreT_c3xuUshjhf6Jc1O1fLtl-OD6vlN9lRJFszR17mAX98Z2YTwV55RVnJMACvaz2kmBQZUFk7zZMgB7pIROIE_q0nE_4b86o2ZV9_nUOU98p6lmuQYMTqjYZl0W3Vvk_ziC3ecs2ZltQUacSMH8ZsKMuzmSxseBT_aghfUtcHOBO9xgq9hpO_6WJkmauOFBjqOex1SmqVFVM32f7b6CsRKi9p1ef-7lRYs9AyXaH8C2BeJ5iRxnS9IO1aaNRKOo0vPn5SNumTb3gSrikeECKTOhqh96jPOF3kods9V84f-9Wm-Y4MHKBlbBPeMVCOV-w1WfieA8DgcS8ioi2KT3a3wNnVfczvLQL7SOT5jBkVdi-s3cuANAuRQazanTNI14F2siOHSyMxWKQlLzNSASD6S8NeNls8XWvTTRqZ_Z6Yx3y0QFlxzpiMf_P7prRcTmvskGQbmG0.I3YAl3m6_lI8atX3VKQNqVRVQ4slInylzpNq48-NtVs"

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