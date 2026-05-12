from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from ..lexicon import lexicon
from ..services import export_audio, ai_translate, giga

start_router = Router()


@start_router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(lexicon.START)


@start_router.message(F.text)
async def link_on_video(message: Message):
    await message.answer('Обрабатываю видео.')
    await message.answer(export_audio.video_to_audio(message.text))
    await message.answer('Определяю текст.')
    await message.answer(ai_translate.ai_translate())
    await message.answer("Делаю конспект")
    await message.answer(giga.giga_text())
