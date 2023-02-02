import requests
import json
from Constants import *

class UserDataDownloader:

    def __init__(self, user, user_url, folderName):
        self.location = RATING_FILE_NAME+user
        self.url = user_url
        self.folderName = folderName

        self.rating = []
        self.ids = []

        self.getPage(self.url)
        self.writeData()

    def getPage(self, url):
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