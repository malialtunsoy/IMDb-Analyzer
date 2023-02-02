import requests
import json

class UserDataDownloader:

    def __init__(self, user, user_url, folderName):
        self.location = "rating-"+user
        self.url = user_url
        self.folderName = folderName

        self.rating = []
        self.ids = []

        self.getPage(self.url)
        self.writeData()

    def getPage(self, url):
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
        self.getData(res)
        button = "<a class=\"flat-button lister-page-next next-page\" href=\""
        nextLinkStart = res.find(button)+len(button)
        nextLink = res[nextLinkStart:res.find(">",nextLinkStart)-1]
        if nextLinkStart-len(button) > 0:
            print("page",int(nextLink[-3:])-100,"-",nextLink[-3:], "downloaded.")
            self.getPage("https://www.imdb.com"+nextLink)

    def getData(self, res):
        start = "<a href=\"/title/"
        end = "</a>"
        startIndex = 0
        endIndex = 0
        while True:
            startIndex = res.find(start,endIndex+1)
            if startIndex < 0:
                break
            endIndex = res.find(end,endIndex+1)
            data = res[startIndex+len(start):endIndex]
            data = data.strip()
            if data == "" or "<img alt" in data:
                if "<img alt" in data:
                    url = data[0:data.find("\"")]
                    url = url.split("/")[0]
                    name = data.split("\"")[2]
                    if url not in self.ids:
                        self.ids.append(url)
                        self.rating.append({"url":url, "name":name})
                
    def writeData(self):

        def name(a):
            return a["name"]
        self.rating.sort(key= name)
        ratingObj = json.dumps(self.rating)
        with open(self.folderName+"/" + self.location,"w") as f:
            f.write(ratingObj)

        for x in self.rating:
            print(x)

        print(len(self.rating) ,"pieces found.")