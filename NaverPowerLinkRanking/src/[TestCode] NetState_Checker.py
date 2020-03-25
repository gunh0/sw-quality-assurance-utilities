import time
import threading
import requests

def net_checker():
    try:
        req = requests.head("https://ad.search.naver.com/search.naver?")
        print("Server: " + req.headers['server'])
        print("Content type: " + req.headers['content-type'])
        print("Date: " + req.headers['Date'])
    except:
        print('error')
    else:
        print('ok')
    finally:
        print('end')
    threading.Timer(1,net_checker).start()

net_checker()
