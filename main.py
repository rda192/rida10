import asyncio
from pytgcalls import idle
from config import call_py
from ππͺπ¨ππ-πΌππ£ πΌπ-πΏπͺπ¬π§π.Ψ§ΩΨͺΨ΄ΨΊΩΩ import arq
async def main():
    await call_py.start()
    print("""    ------------------
   | ΩΩΩΨ²Ω Ψ§Ψ¨Ω Ψ§ΩΨ―ΩΨ±Ψ© Ψ΄ΨΊΨ§Ω  ! |
    ------------------"""    )
    await idle()
    await arq.close()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
