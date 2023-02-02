import requests
import json
import os 
from Constants import *

class PieceDownloader:
    def __init__(self, user, folderName):
        self.folderName = folderName
        self.user = user
        self.rating_file = RATING_FILE_NAME+user

    def getPiece(self, url):
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

    def processData(self, data):
        ret = {}
        
        time = 0
        genres = []
        cast = []
        directors = []
        countries = []

        if not "aboveTheFoldData" in data["props"]["pageProps"].keys():
            return False

        title = data["props"]["pageProps"]["aboveTheFoldData"]["titleText"]["text"]
        rate = data["props"]["pageProps"]["aboveTheFoldData"]["ratingsSummary"]["aggregateRating"]
        ret["rating"] = rate
        ret[ID] = data["props"]["pageProps"]["tconst"]

        if data["props"]["pageProps"]["aboveTheFoldData"]["canHaveEpisodes"]:
            ret[IS_SERIES] = True
        else:
            ret[IS_SERIES] = False

        if data["props"]["pageProps"]["aboveTheFoldData"]["runtime"]:
            avrTime = data["props"]["pageProps"]["aboveTheFoldData"]["runtime"]["seconds"]
            if data["props"]["pageProps"]["aboveTheFoldData"]["canHaveEpisodes"]:
                numOfEpisodes = data["props"]["pageProps"]["mainColumnData"]["episodes"]["episodes"]["total"]
                ret["avrgTime"] = avrTime
                ret["episodeCount"] = numOfEpisodes
                time += numOfEpisodes * avrTime
                
            else:
                time += avrTime
        else:
            print("Something missing in: " + title)

        #GENRE
        for genre in data["props"]["pageProps"]["aboveTheFoldData"][GENRES][GENRES]:
            genres.append(genre["text"])
        #CAST
        for actor in data["props"]["pageProps"]["mainColumnData"][CAST]["edges"]:
            name = actor["node"]["name"]["nameText"]["text"]
            cast.append(name)
        #DIRECTOR
        for director in data["props"]["pageProps"]["mainColumnData"][DIRECTORS]:
            for direc in director["credits"]:
                name = direc["name"]["nameText"]["text"]
                directors.append(name)
        #COUNTRY
        if not data["props"]["pageProps"]["aboveTheFoldData"]["series"]:
            for country in data["props"]["pageProps"]["aboveTheFoldData"]["countriesOfOrigin"][COUNTRIES]:
                countries.append(country[ID])

        ret[TITLE] = title
        ret[TIME] = time
        ret[GENRES] = genres
        ret[CAST] = cast
        ret[DIRECTORS] = directors
        ret[COUNTRIES] = countries

        return ret
        

    def downloadUserPieces(self):
        print("DOWNLOADING DATA OF PIECES:")
        rating = []
        f = open(self.folderName+"/"+self.rating_file, "r")
        rating = json.load(f)

        pieces = []

        for piece in rating:
            id = piece["url"].split("/")[0]
            if not os.path.exists(os.path.join(os.getcwd()+"/"+self.folderName+"/"+PIECES_STORAGE_FILE_NAME+"/", id)):
                data = self.getPiece(piece["url"])
                data = self.processData(data)
                print(id, data[TITLE])
                with open(self.folderName+"/"+PIECES_STORAGE_FILE_NAME+"/"+id,"w") as f:
                    f.write(json.dumps(data))
        print("DOWNLOAD FINISHED.")
        


    