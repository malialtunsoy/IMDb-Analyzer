from UserDataDownloader import *
from PieceDownloader import *
from AnalysisMaker import *

import sys
import os
from Constants import *
from UserWatchlistDownloader import UserWatchlistDownloader

class IMDb_Analayzer:

    def __init__(self, user, userURL = "", command = ""):
        self.user = user
        self.userURL = userURL
        dataDirectoryName = DATA_FILE_NAME
        
        self.createDataDirectory(dataDirectoryName)
        if not userURL == "":
            if command == "-wl":
                UserWatchlistDownloader(self.user,self.userURL)
            else:
                UserDataDownloader(self.user, self.userURL, dataDirectoryName)
        pieceDownloader = PieceDownloader(self.user, dataDirectoryName)
        pieceDownloader.downloadUserPieces()
        analysisMaker = AnalysisMaker(self.user, dataDirectoryName)
        analysisMaker.makeAnalysis()
        analysisMaker.printAnalysis()

    def createDataDirectory(self, dataDirectoryName):
        if not os.path.exists(os.path.join(os.getcwd(),dataDirectoryName)):
            os.makedirs(os.path.join(os.getcwd(),dataDirectoryName))
            os.makedirs(os.path.join(os.getcwd(),dataDirectoryName,PIECES_STORAGE_FILE_NAME))


if len(sys.argv) == 2:
    IMDb_Analayzer(sys.argv[1])
elif len(sys.argv) == 3:
    IMDb_Analayzer(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 4:
    IMDb_Analayzer(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print("Wrong input!")
        