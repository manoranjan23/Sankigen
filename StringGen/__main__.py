import asyncio
import importlib

from pyrogram import idle

from StringGen import LOGGER, Shilpa
from StringGen.modules import ALL_MODULES


async def Shilpa_boot():
    try:
        await Shilpa.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("StringGen.modules." + all_module)

    LOGGER.info(f"@{Shilpa.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(Shilpa_boot())
    LOGGER.info("Stopping String Gen Bot...")
