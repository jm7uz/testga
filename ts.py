
url = input("url: ")
import aiohttp
import asyncio

 
async def main(url):
    web_url = "https://save-from.net/api/convert"
    data ={"url":url}

    headers = {'content-type' : 'application/json', 
        'referer':'https://save-from.net/', 
        'Origin': 'https://save-from.net',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=web_url, params=data) as resp:
            print(resp.status)
            try:
                
                r = await resp.json()
                print(r)
                id = r['id'] if 'id' in r else None
                manzil = r['url'] if 'url' in r else None
                info = r['meta'] if 'meta' in r else None
                print(manzil)
            except Exception as e:
                print(e)

asyncio.run(main(url=url))

#salom dunyo
