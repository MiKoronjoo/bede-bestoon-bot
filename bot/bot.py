from pyrogram import Client


class Bot(Client):
    ADMIN_ID = 0

    def __init__(self, db):
        name = self.__class__.__name__.lower()
        super().__init__(
            session_name=f'{name}.session',
            config_file='bot.ini',
            workers=16,
            plugins=dict(
                root="bot.plugins",
                exclude=["start"]
            ),
            sleep_threshold=180
        )
        self.db = db

    async def start(self):
        await super().start()

        me = await self.get_me()
        print(f"Bot started on @{me.username}")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped")
