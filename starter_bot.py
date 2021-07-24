from chai_py import ChaiBot, Update


class Bot(ChaiBot):
    def setup(self):
        self.logger.info("Setting up...")

    async def on_message(self, update: Update) -> str:
        return "Hi, I'm Chess Bot."
