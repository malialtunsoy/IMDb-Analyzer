import requests
import json
import os 

rating = []
rating_file = "rating"
pieces_folder = "pieces/"
f = open("datas/"+rating_file, "r")
rating = json.load(f)

pieces = []

def getPiece(url):
    url = "https://www.imdb.com/title/" + url
    payload={}
    headers = {
    'authority': 'www.imdb.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.text
    start = "type=\"application/json\">"
    end = "</script><script>"
    startIndex = res.find(start)
    data = res[startIndex+len(start):res.find(end,startIndex)]
    return json.loads(data)

for piece in rating:
    id = piece["url"].split("/")[0]
    if not os.path.exists(os.path.join(os.getcwd()+"datas/", pieces_folder, id)):
        data = getPiece(piece["url"])
        print(id)
        with open("datas/"+pieces_folder+id,"w") as f:
            f.write(json.dumps(data))
    