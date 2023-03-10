from re import T
import requests
import json
from Constants import *

class AnalysisMaker:
    def __init__(self, user, folderName):
        self.folderName = folderName
        self.user = user
        self.rating_file = RATING_FILE_NAME+user
        self.time = 0
        self.series = 0
        self.movies = 0
        self.movieTime = 0
        self.seriesTime = 0
        self.genres = {}
        self.movieGenres = {}
        self.seriesGenres = {}
        self.cast = {}
        self.directors = {}
        self.countries = {}

        self.totalRating = 0
        self.movieRating = 0
        self.seriesRating = 0

        self.longestMovieDuration = 0
        self.longestMovieName = ""

        self.longestSeriesDuration = 0
        self.longestSeriesName = ""

        self.mostEpisodeCount = 0
        self.mostEpisodeSeries = ""
    
    def makeAnalysis(self):
        rating = []
        f = open(self.folderName+"/"+self.rating_file, "r")
        rating = json.load(f)

        for rate in rating:
            try:
                id = rate["url"].split("/")[0]
                f = open(self.folderName+"/"+PIECES_STORAGE_FILE_NAME+"/"+id,"r")
                data = json.load(f)
                title = data[TITLE]

                if data[IS_SERIES]:
                    self.time += data[TIME]
                    self.series += 1
                    self.seriesTime += data[TIME]
                    self.seriesRating += data[RATING]
                    if data[EPISODE_COUNT] > self.mostEpisodeCount:
                        self.mostEpisodeCount = data[EPISODE_COUNT]
                        self.mostEpisodeSeries = data[TITLE]

                    if data[TIME] > self.longestSeriesDuration:
                        self.longestSeriesDuration = data[TIME]
                        self.longestSeriesName = data[TITLE]
                    #GENRE
                    for genre in data[GENRES]:
                        if genre in self.seriesGenres.keys():
                            self.seriesGenres[genre] += 1
                        else:
                            self.seriesGenres[genre] = 1
                else:
                    self.time += data[TIME]
                    self.movies += 1
                    self.movieTime += data[TIME]
                    self.movieRating += data[RATING]
                    if data[TIME] > self.longestMovieDuration:
                        self.longestMovieDuration = data[TIME]
                        self.longestMovieName = data[TITLE]
                    #GENRE
                    for genre in data[GENRES]:
                        if genre in self.movieGenres.keys():
                            self.movieGenres[genre] += 1
                        else:
                            self.movieGenres[genre] = 1
                self.totalRating += data[RATING]
                #GENRE
                for genre in data[GENRES]:
                    if genre in self.genres.keys():
                        self.genres[genre] += 1
                    else:
                        self.genres[genre] = 1
                #CAST
                for actor in data[CAST]:
                    if actor in self.cast.keys():
                        self.cast[actor] += 1
                    else:
                        self.cast[actor] = 1
                #DIRECTOR
                for director in data[DIRECTORS]:
                    if director in self.directors.keys():
                        self.directors[director] += 1
                    else:
                        self.directors[director] = 1
                #COUNTRY
                for country in data[COUNTRIES]:
                    if country in self.countries.keys():
                        self.countries[country] += 1
                    else:
                        self.countries[country] = 1
            except Exception as inst:
                print("Something went wrong:", id, title)
                print(inst)

            f.close()

    def convertTime(self, time):

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

    def convertTimeToString(self, time):
        return (str(time["days"]) + " days " + str(time["hours"])+" hours "+ str(time["minutes"])+" minutes")

    def printAnalysis(self):
        print("\n==== IMDb ANALYSIS OF " + (self.user).upper() + " ====")
        print(self.movies, "movies watched.")
        print(self.series, "series watched.")
        print("")
        print("=== RATINGS ===")
        print("Overall rating:", round(self.totalRating/(self.movies+self.series),1))
        print("Overall movie rating:", round(self.movieRating/self.movies,1))
        print("Overall series rating:", round(self.seriesRating/self.series,1))
        print("")
        print("=== TOTAL WATCH TIME ===")
        totalTime = self.convertTime(self.time)
        print(totalTime["days"],"days", totalTime["hours"], "hours", totalTime["minutes"],"minutes")
        print("=== MOVIES WATCH TIME ===")
        movieTime = self.convertTime(self.movieTime)
        print(movieTime["days"],"days", movieTime["hours"], "hours", movieTime["minutes"],"minutes")
        print("=== SERIES WATCH TIME ===")
        seriesTime = self.convertTime(self.seriesTime)
        print(seriesTime["days"],"days", seriesTime["hours"], "hours", seriesTime["minutes"],"minutes")
        print("")
        print("=== LONGEST MOVIE YOU WATCHED ===")
        print(self.longestMovieName, "-", self.convertTimeToString(self.convertTime(self.longestMovieDuration)))
        print("=== LONGEST SERIES YOU WATCHED ===")
        print(self.longestSeriesName, "-", self.convertTimeToString(self.convertTime(self.longestSeriesDuration)))
        print("=== SERIES WITH MOST EPISODES ===")
        print(self.mostEpisodeSeries, "-", self.mostEpisodeCount, "episodes")

        print("")
        print("====== FAVORITE GENRES TOTAL ======")
        totalGenres = 0
        genresList = []
        for genre in self.genres.keys():
            totalGenres += self.genres[genre]
            genresList.append({"genre": genre, "count": self.genres[genre]})
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
        for genre in self.movieGenres.keys():
            totalGenres += self.movieGenres[genre]
            genresList.append({"genre": genre, "count": self.movieGenres[genre]})
        genresList.sort(key=genreSort, reverse=True)
        print( "{:<15} {:<13} {:<3}".format("GENRE", "PERCENTAGE(%)", "COUNT") )
        for genre in genresList:
            print( "{:<15} {:<13} {:<3}".format(genre["genre"], round((genre["count"]/totalGenres)*100, 2), genre["count"]) )

        print("")
        print("====== FAVORITE SERIES GENRES ======")
        totalGenres = 0
        genresList = []
        for genre in self.seriesGenres.keys():
            totalGenres += self.seriesGenres[genre]
            genresList.append({"genre": genre, "count": self.seriesGenres[genre]})
        genresList.sort(key=genreSort, reverse=True)
        print( "{:<15} {:<13} {:<3}".format("GENRE", "PERCENTAGE(%)", "COUNT") )
        for genre in genresList:
            print( "{:<15} {:<13} {:<3}".format(genre["genre"], round((genre["count"]/totalGenres)*100, 2), genre["count"]) )

        print("")

        print("====== MOST WATCHED CAST ======")
        castList = []
        for actor in self.cast.keys():
            castList.append({"actor": actor, "count": self.cast[actor]})
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
        for director in self.directors.keys():
            directorList.append({"name": director, "count": self.directors[director]})
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
        for country in self.countries.keys():
            countryList.append({"name": country, "count": self.countries[country]})
        def countrySort(a):
            return a["count"]
        countryList.sort(key=countrySort, reverse=True)
        print( "{:<2} {:<8} {:<3}".format("#","COUNTRY", "COUNT") )
        index = 1
        for country in countryList[:min(30,len(countryList))]:
            print( "{:<2} {:<8} {:<3}".format(index, country["name"], country["count"]) )
            index += 1
