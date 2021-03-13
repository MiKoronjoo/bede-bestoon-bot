from pyrogram import filters
from pyrogram.types import Message

from ..bot import Bot


@Bot.on_message(filters.command('start'))
async def start(bot: Bot, message: Message):
    pass
