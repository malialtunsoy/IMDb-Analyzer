import requests
import json

rating = []
location = "rating"
link = "https://www.imdb.com/user/ur111111/watchlist"

def getPage(url):
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
    getData(res)
    

def getData(res):
    start = "IMDbReactInitialState.push("
    end = ");\n    </script>"
    startIndex = 0
    endIndex = 0
    startIndex = res.find(start,endIndex+1)
    endIndex = res.find(end,startIndex+1)
    data = res[startIndex+len(start):endIndex]
    data = json.loads(data)
    for piece in data["list"]["items"]:
        id = piece["const"]
        rating.append({"url": id, "name":"-"})

            
    
getPage(link)

ratingObj = json.dumps(rating)
with open("datas/"+location,"w") as f:
    f.write(ratingObj)

for x in rating:
    print(x)

print(len(rating))