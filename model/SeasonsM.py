class Seasons:

    def __init__(self, __seasons_id):
        self.__seasons_id = __seasons_id

    def setSeasonId(self, seasons_id) -> None:
        self.__seasons_id = seasons_id
    def getSeasonId(self) -> int:
        return self.__seasons_id