class Equipes:

    def __init__(self):
        self.__equipe_id = None,
        self.__nom_de_equipe = None,
        self.__manager = None,
        self.__joueurs = None

    def setEquipeId(self, equipe_id) -> None:
        self.__equipe_id = equipe_id

    def getEquipeId(self) -> int:
        return self.__equipe_id
    
    def setNomDeEquipe(self, nom_de_equipe) -> None:
        self.__nom_de_equipe = nom_de_equipe
    
    def getNomDeEquipe(self) -> str:
        return self.__nom_de_equipe
    
    def setManager(self, manager) -> None:
        self.__manager = manager

    def getManager(self) -> str:
        return self.__manager
    
    def setJoueurs(self, joueurs) -> None:
        self.__joueurs = joueurs

    def getJoueurs(self) -> str:
        return self.__joueurs


