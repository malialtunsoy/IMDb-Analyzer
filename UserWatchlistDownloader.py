import requests
import json
from Constants import *

class UserWatchlistDownloader:
    
    def __init__(self, user, url):
        self.rating = []
        self.location = RATING_FILE_NAME+user

        self.getPage(url)
        self.writeData()


    def getPage(self, url):
        response = requests.request("GET", url, headers=headers, data=payload)
        res = response.text
        self.getData(res)
        

    def getData(self, res):
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
            self.rating.append({"url": id, "name":"-"})

    def writeData(self):
        def name(a):
            return a["name"]
        self.rating.sort(key= name)
        ratingObj = json.dumps(self.rating)
        with open(DATA_FILE_NAME+"/"+self.location,"w") as f:
            f.write(ratingObj)

        for x in self.rating:
            print(x)

        print(len(self.rating) ,"pieces found.")