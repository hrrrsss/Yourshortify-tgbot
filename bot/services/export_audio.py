import yt_dlp 
import subprocess #ffmpeg-python библиотека
import os
from pathlib import Path

def video_to_audio(link: str):
    # Получаем путь к папке files относительно текущего файла
    # Предполагаем, что структура такая:
    # project/
    # ├── services/export_audio.py (этот файл)
    # └── files/ (папка для файлов)
    
    current_dir = Path(__file__).parent  # services/
    files_dir = current_dir.parent / "files"  # поднимаемся на уровень выше, затем в files/
    
    # Создаем папку files если ее нет
    files_dir.mkdir(exist_ok=True)
    
    # Пути к файлам
    temp_video_path = files_dir / "temp_video.mp4"
    audio_path = files_dir / "audio.mp3"
    
    rutube_url = link

    # Скачиваем видео
    ydl_opts = {
        'format': 'best[ext=mp4]/best', 
        'outtmpl': str(temp_video_path)  # правильный путь
    }
    print("📥 Скачиваю...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([rutube_url])

    # Конвертируем в MP3
    print("🎵 Конвертирую...")
    subprocess.run([
        'ffmpeg', '-i', str(temp_video_path),
        '-q:a', '0', '-map', 'a', str(audio_path),
        '-y', '-loglevel', 'error'
    ])

    # Удаляем MP4
    if temp_video_path.exists():
        temp_video_path.unlink()
        print("🗑 Удалил временный MP4")

    if audio_path.exists():
        print(f"✅ Готово: {audio_path}")
    else:
        print("❌ Не вышло")
    
    return "выполнено"