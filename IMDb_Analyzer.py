from UserDataDownloader import *
from PieceDownloader import *
from AnalysisMaker import *

import sys
import os

class IMDb_Analayzer:

    def __init__(self, user, userURL):
        self.user = user
        self.userURL = userURL
        dataDirectoryName = "datas"
        
        self.createDataDirectory(dataDirectoryName)
        userDataDownloader = UserDataDownloader(self.user, self.userURL, dataDirectoryName)
        pieceDownloader = PieceDownloader(self.user, dataDirectoryName)
        pieceDownloader.downloadUserPieces()
        analysisMaker = AnalysisMaker(self.user, dataDirectoryName)
        analysisMaker.makeAnalysis()
        analysisMaker.printAnalysis()

    def createDataDirectory(self, dataDirectoryName):
        if not os.path.exists(os.path.join(os.getcwd(),dataDirectoryName)):
            os.makedirs(os.path.join(os.getcwd(),dataDirectoryName))
            os.makedirs(os.path.join(os.getcwd(),dataDirectoryName,"pieces"))


IMDb_Analayzer(sys.argv[1], sys.argv[2])
        