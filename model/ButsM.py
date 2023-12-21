class Buts:

    def __init__(self):
        self.__but_id = None,
        self.__minute = None,
        self.__buteur = None,
        self.__passeur = None
    
    def setButId(self, but_id) -> None:
        self.__but_id = but_id
    def getButId(self) -> int:
        return self.__but_id

    def setMinute(self, minute) -> None:
        self.__minute = minute
    def getMinute(self) -> int:
        return self.__minute
    
    def setButeur(self, buteur) -> None:
        self.__buteur = buteur
    def getButeur(self) -> str:
        return self.__buteur
    
    def setPasseur(self, passeur) -> None:
        self.__passeur = passeur
    def getPasseur(self) -> str:
        return self.__passeur