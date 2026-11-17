import asyncio
import findyoutubevideo

async def main():
    result = await findyoutubevideo.search("D5F6DFJg4HE")
    print(result)

asyncio.run(main())