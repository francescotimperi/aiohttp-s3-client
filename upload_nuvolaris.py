import aiohttp
import asyncio
from aiohttp_s3_client import S3Client

async def run():
    client = S3Client(url="http://localhost",
                      session=aiohttp.ClientSession(),
                      access_key_id="nuvolaris",
                      secret_access_key="<pwd>",
                      extra_context='/api/upload',
                      region='us-east-1')

    async with await client.put("nuvolaris-web/pippo/test.txt", "this is a text a bit more longer") as resp:
        print(resp)


def main():

    asyncio.run(run())                      

if __name__ == "__main__":
   main()