from pyrogram import filters
from pyrogram.types import Message

from ..bot import Bot


@Bot.on_message(filters.private)
async def message_handler(bot: Bot, message: Message):
    pass
