import yt_dlp 
import subprocess #ffmpeg-python скачать 
import os

rutube_url = "https://rutube.ru/video/73749632ebab889ef9463dc9b3b9a107/"  # вставь ссылку

# Скачиваем видео
ydl_opts = {'format': 'best[ext=mp4]/best', 'outtmpl': 'temp_video.mp4'}
print("📥 Скачиваю...")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([rutube_url])

# Конвертируем в MP3
print("🎵 Конвертирую...")
subprocess.run([
    'ffmpeg', '-i', 'temp_video.mp4',
    '-q:a', '0', '-map', 'a', 'audio.mp3',
    '-y', '-loglevel', 'error'
])

# Удаляем MP4
if os.path.exists('temp_video.mp4'):
    os.remove('temp_video.mp4')
    print("🗑 Удалил временный MP4")

if os.path.exists('audio.mp3'):
    print("✅ Готово: audio.mp3")
else:
    print("❌ Не вышло")