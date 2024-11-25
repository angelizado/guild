import asyncio
from utils.config import load
from utils.updater import start
from utils.utils import clear, welcome
import sys

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main():
    clear()
    welcome()
    config = load("config.json")
    await start(config)



if __name__ == "__main__":
    asyncio.run(main())

