class Matchs:

    def __init__(self, __math_id, __date, __stade, __resultat):
        self.__math_id = __math_id,
        self.__date = __date,
        self.__stade = __stade,
        self.__resultat = __resultat

    def setMathId(self, math_id) -> None:
        self.__math_id = math_id
    def getMathId(self) -> int:
        return self.__math_id
    
    def setDate(self, date) -> None:
        self.__date = date
    def getDate(self) -> str:
        return self.__date
    
    def setStade(self, stade) -> None:
        self.__stade = stade
    def getStade(self) -> str:
        return self.__stade
    
    def setResultat(self, resultat) -> None:
        self.__resultat = resultat
    def getResultat(self) -> str:
        return self.__resultat
    
    
