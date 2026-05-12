import requests

def giga_text():
    # 1. Токен с сайта gigachat.dev
    ACCESS_TOKEN = "eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.j3Dra7aQCCqfLneVgwx0ci55vQHaMVmi7SiIWb4Mz3zsS4AigM6jouW_phrQWsJC-MDRex5Qx4h1GYaz314LAmSmgfScZfMwdOria61xZDrdZfrgqGP735Xt2Uw4NulNv2lZHlKOCGlY7F5pGeI8eX_iJL0bbIJGywjK2g4Zv9sXA3V5DX6VN3yLPG3cosCSmpwakF04OJ8zZNG9HduT_mTJMWaOhKtlv1tp6iuvs5sug7TU68spDlLTqaq9NUPwjlLYaZnK3Lk6R2aFZt17eu3jvqTa8RgIVSd9E0rgBDD4qZ4pR2LgO7eAPBUPIbCVcC0jiGMiUwu3D3o7JRsAmQ.fkkZ81HQJdtgVWRZUCVp0Q.uAbcmqZMsBSmbInaty6sD8O4OTXxgfKx4_2yaWvmHiehKTaXe49_hHOm4NjqIUaS-pqLy3qUVDGDvWXSVyVqjQrAjN_gPFLGnJ4NStJfsJGjj7cQMu9FTQH2YxHjfnwu4ViLaMY-aKSqhGZHa7w0az236WctLqQWyNAilT7yBBboLKVWHOn0WOeAcLV53EGjOIXIes-CTGFm_eJro8Tweom9WCYVUUxA_-KYk-zStCWIsnt_tmtVR5DDMYRqOOP0HvQhmaWVcxm4BR5Bs4k2OTmm6uHaaLv7mS6qxmzGBybNqfP5gG29tRoJxpeGeiBUU4Ce1e0WehplypJEF2lREz9V2d8MYRGY-I79D7H_hmr1LL9y3UaVzdHSH-vbbFEaCpfcUlYFx8iIoeYPfcEKHD__SC9lVmXQfEY45ZSVhlELnzkDTGVESjnb9mZKXQ7orjvd_2LrgIZykvO6SrGJPx6c8pgkWWVikQSp7xOtwLooBU2mUHLkUqyjGow1OVTDKwF-tkgYbV9hMNCbkVSGWGcGqLCciaJ0WjPfIOjBaTiFPuW1mB5vNAN9RrcS4DgP1uxIqveZ0Fz5ukPIIrAvOqaDKsnOkHZgBjxqIhL9omKv7QNKkbLwiTAMc1jY5zeXB0oIGZ0xYZQt0J1xrmo2onMX9fs6wBV_jT3dt1h5HDX-fHgd23fDdDpTRbgg7JkGnPhb_LoMsuvi8FFhVTNohs2uMunVUxp9lsXXiFtLU4M.f2jbDIA-v4SK9jX6bzJ0kAHkOzmpRGB0wcrpkWuL4QM"

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
        
    else:
        print(f"❌ Ошибка {response.status_code}: {response.text}")