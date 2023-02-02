from UserDataDownloader import *
from PieceDownloader import *
from AnalysisMaker import *

import sys
import os

class IMDb_Analayzer:

    def __init__(self, user, userURL):
        self.user = user
        self.userURL = userURL
        folderName = "data"
        
        self.createDataDirectory()
        userDataDownloader = UserDataDownloader(self.user, self.userURL, folderName)
        pieceDownloader = PieceDownloader(self.user, folderName)
        pieceDownloader.downloadUserPieces()
        analysisMaker = AnalysisMaker(self.user, folderName)
        analysisMaker.makeAnalysis()
        analysisMaker.printAnalysis()

    def createDataDirectory(self, folderName):
        if os.path.exists(os.path.join(os.getcwd(),folderName)):
            os.makedirs(os.path.join(os.getcwd(),folderName))


IMDb_Analayzer(sys.argv[1], sys.argv[2])
        