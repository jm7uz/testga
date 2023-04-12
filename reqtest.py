import requests


from urllib.request import Request, urlopen
from threading import Thread
from ssl import _create_default_https_context

class yuklagich (Thread):
    def __init__(self, url, name) -> None:
        Thread.__init__(self)
        self.name = name
        self.url = url
        self.__bufsize = 6555
    @property
    def Url(self):
        return self.url
    
    @property
    def BuzSize(self):
        return self.__bufsize
    
    def run(self) -> None:
        domain = Request(self.url)
        context = _create_default_https_context()
        domain.add_header("User-agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0")
        file = urlopen(domain, context=context)
        with open(file=f"{self.name}.mp4", mode="wb") as f:
            exit = False
            while not exit:
                qism = file.read(self.__bufsize)
                if qism:
                    f.write(qism)
                else:
                    exit = True
class Worker:
    def __init__(self) -> None:
        self.urls = []
    def add_url(self, url):
        self.urls.append(url)
    def start(self, name):
        ths = []
        for url in self.urls:
            th = yuklagich(url, name)
            th.start()
            ths.append(th)
        exit = False
        while not exit:
            exit = True
            for th in ths:
                if th.is_alive():
                    exit = False

    









def saverapi(url):
    headers = {'content-type' : 'application/json', 
        'referer':'https://save-from.net/', 
        'Origin': 'https://save-from.net',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    data ={"url":url}
    url = ("https://save-from.net/api/convert")
    r = requests.post(url, params=data, headers=headers)
    try:
        r = r.json()
        id = r['id'] if 'id' in r else None
        manzil = r['url'] if 'url' in r else None
        info = r['meta'] if 'meta' in r else None
        print(info)
        return manzil
    except Exception as e:
        print(e)
    

ur = saverapi(url=input("url: "))
down = Worker()
down.add_url(ur[0]['url'])
down.start(name="meta")