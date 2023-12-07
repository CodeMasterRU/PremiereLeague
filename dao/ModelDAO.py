from abc import ABC, abstractmethod
from dao.ConnectionDAO import ConnexionBD

class modeleDAO(ABC):
    connect_odjet = ConnexionBD().getConnexion() 

    # insert

    @abstractmethod
    def insererUn(self, objIns) -> int:
        pass

