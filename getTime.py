import requests
import json

rating_file = "rating"
pieces_folder = "pieces/"

rating = []
f = open("datas/"+rating_file, "r")
rating = json.load(f)

time = 0
series = 0
movies = 0
movieTime = 0
seriesTime = 0
genres = {}
movieGenres = {}
seriesGenres = {}
cast = {}
directors = {}
countries = {}

for rate in rating:
    id = rate["url"].split("/")[0]
    f = open("datas/"+pieces_folder+id,"r")
    data = json.load(f)
    if not "aboveTheFoldData" in data["props"]["pageProps"].keys():
        f.close()
        input(id)
        continue
    title = data["props"]["pageProps"]["aboveTheFoldData"]["titleText"]["text"]
    if data["props"]["pageProps"]["aboveTheFoldData"]["runtime"]:
        avrTime = data["props"]["pageProps"]["aboveTheFoldData"]["runtime"]["seconds"]
        if data["props"]["pageProps"]["aboveTheFoldData"]["canHaveEpisodes"]:
            numOfEpisodes = data["props"]["pageProps"]["mainColumnData"]["episodes"]["episodes"]["total"]
            time += numOfEpisodes * avrTime
            series += 1
            seriesTime += numOfEpisodes * avrTime
            #GENRE
            for genre in data["props"]["pageProps"]["aboveTheFoldData"]["genres"]["genres"]:
                if genre["text"] in seriesGenres.keys():
                    seriesGenres[genre["text"]] += 1
                else:
                    seriesGenres[genre["text"]] = 1
        else:
            time += avrTime
            movies += 1
            movieTime += avrTime
            #GENRE
            for genre in data["props"]["pageProps"]["aboveTheFoldData"]["genres"]["genres"]:
                if genre["text"] in movieGenres.keys():
                    movieGenres[genre["text"]] += 1
                else:
                    movieGenres[genre["text"]] = 1
    else:
        input(id)
    
    #GENRE
    for genre in data["props"]["pageProps"]["aboveTheFoldData"]["genres"]["genres"]:
        if genre["text"] in genres.keys():
            genres[genre["text"]] += 1
        else:
            genres[genre["text"]] = 1
    #CAST
    for actor in data["props"]["pageProps"]["mainColumnData"]["cast"]["edges"]:
        name = actor["node"]["name"]["nameText"]["text"]
        if name in cast.keys():
            cast[name] += 1
        else:
            cast[name] = 1
    #DIRECTOR
    for director in data["props"]["pageProps"]["mainColumnData"]["directors"]:
        for direc in director["credits"]:
            name = direc["name"]["nameText"]["text"]
            if name in directors.keys():
                directors[name] += 1
            else:
                directors[name] = 1
    #COUNTRY
    if not data["props"]["pageProps"]["aboveTheFoldData"]["series"]:
        for country in data["props"]["pageProps"]["aboveTheFoldData"]["countriesOfOrigin"]["countries"]:
            if country["id"] in countries.keys():
                countries[country["id"]] += 1
            else:
                countries[country["id"]] = 1
    f.close()

def convertTime(time):

    seconds = time % 60
    minutes = (time-seconds) / 60
    temp_minutes = minutes % 60
    hours = (minutes - temp_minutes) / 60
    minutes = temp_minutes
    temp_hours = hours % 24
    days = (hours - temp_hours) / 24
    hours = temp_hours

    days, hours, minutes = int(days), int(hours), int(minutes)

    return {"days":days, "hours":hours, "minutes":minutes}


print(movies, "movies")
print(series, "series")
print("")
print("=== TOTAL ===")
totalTime = convertTime(time)
print(totalTime["days"],"days", totalTime["hours"], "hours", totalTime["minutes"],"minutes")
print("=== MOVIES ===")
movieTime = convertTime(movieTime)
print(movieTime["days"],"days", movieTime["hours"], "hours", movieTime["minutes"],"minutes")
print("=== SERIES ===")
seriesTime = convertTime(seriesTime)
print(seriesTime["days"],"days", seriesTime["hours"], "hours", seriesTime["minutes"],"minutes")

print("")
print("====== FAVORITE GENRES TOTAL ======")
totalGenres = 0
genresList = []
for genre in genres.keys():
    totalGenres += genres[genre]
    genresList.append({"genre": genre, "count": genres[genre]})
def genreSort(a):
    return a["count"]
genresList.sort(key=genreSort, reverse=True)
print( "{:<15} {:<13} {:<3}".format("GENRE", "PERCENTAGE(%)", "COUNT") )
for genre in genresList:
    print( "{:<15} {:<13} {:<3}".format(genre["genre"], round((genre["count"]/totalGenres)*100, 2), genre["count"]) )

print("")
print("====== FAVORITE MOVIE GENRES ======")
totalGenres = 0
genresList = []
for genre in movieGenres.keys():
    totalGenres += movieGenres[genre]
    genresList.append({"genre": genre, "count": movieGenres[genre]})
genresList.sort(key=genreSort, reverse=True)
print( "{:<15} {:<13} {:<3}".format("GENRE", "PERCENTAGE(%)", "COUNT") )
for genre in genresList:
    print( "{:<15} {:<13} {:<3}".format(genre["genre"], round((genre["count"]/totalGenres)*100, 2), genre["count"]) )

print("")
print("====== FAVORITE SERIES GENRES ======")
totalGenres = 0
genresList = []
for genre in seriesGenres.keys():
    totalGenres += seriesGenres[genre]
    genresList.append({"genre": genre, "count": seriesGenres[genre]})
genresList.sort(key=genreSort, reverse=True)
print( "{:<15} {:<13} {:<3}".format("GENRE", "PERCENTAGE(%)", "COUNT") )
for genre in genresList:
    print( "{:<15} {:<13} {:<3}".format(genre["genre"], round((genre["count"]/totalGenres)*100, 2), genre["count"]) )

print("")

print("====== MOST WATCHED CAST ======")
castList = []
for actor in cast.keys():
    castList.append({"actor": actor, "count": cast[actor]})
def actorSort(a):
    return a["count"]
castList.sort(key=actorSort, reverse=True)
print( "{:<2} {:<30} {:<3}".format("#","ACTOR", "COUNT") )
index = 1
for actor in castList[:min(30,len(castList))]:
    print( "{:<2} {:<30} {:<3}".format(index, actor["actor"], actor["count"]) )
    index += 1

print("")

print("====== MOST WATCHED DIRECTOR ======")
directorList = []
for director in directors.keys():
    directorList.append({"name": director, "count": directors[director]})
def directorSort(a):
    return a["count"]
directorList.sort(key=directorSort, reverse=True)
print( "{:<2} {:<30} {:<3}".format("#","DIRECTOR", "COUNT") )
index = 1
for director in directorList[:min(30,len(directorList))]:
    print( "{:<2} {:<30} {:<3}".format(index, director["name"], director["count"]) )
    index += 1

print("")

print("====== MOST WATCHED COUNTRY PRODUCTION ======")
countryList = []
for country in countries.keys():
    countryList.append({"name": country, "count": countries[country]})
def countrySort(a):
    return a["count"]
countryList.sort(key=countrySort, reverse=True)
print( "{:<2} {:<8} {:<3}".format("#","COUNTRY", "COUNT") )
index = 1
for country in countryList[:min(30,len(countryList))]:
    print( "{:<2} {:<8} {:<3}".format(index, country["name"], country["count"]) )
    index += 1
