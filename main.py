import asyncio
from pytgcalls import idle
from config import call_py
from 𝙈𝙪𝙨𝙞𝙘-𝘼𝙗𝙣 𝘼𝙇-𝘿𝙪𝙬𝙧𝙖.التشغيل import arq
async def main():
    await call_py.start()
    print("""    ------------------
   | ميوزك ابن الدورة شغال  ! |
    ------------------"""    )
    await idle()
    await arq.close()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
