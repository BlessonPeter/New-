from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.flipkart.com/fire-boltt-epic-plus-with1-83-2-5d-curved-glass-spo2-heart-rate-tracking-touchscreen-smartwatch/p/itm681ecd1fc9d01?pid=SMWGGZ746XUPRH3N&fm=organic&ppt=dynamic&ppn=dynamic&ssid=nixeo5bun40000001717177001650"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive"
}

response = requests.get(url)
print(response.status_code)
