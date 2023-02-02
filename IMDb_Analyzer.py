from UserDataDownloader import *
from PieceDownloader import *
from AnalysisMaker import *

import sys

class IMDb_Analayzer:

    def __init__(self, user, userURL):
        self.user = user
        self.userURL = userURL

        userDataDownloader = UserDataDownloader(self.user, self.userURL)
        pieceDownloader = PieceDownloader(self.user)
        pieceDownloader.downloadUserPieces()
        analysisMaker = AnalysisMaker(self.user)
        analysisMaker.makeAnalysis()
        analysisMaker.printAnalysis()

IMDb_Analayzer(sys.argv[1], sys.argv[2])
        