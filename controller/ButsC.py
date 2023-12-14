from dao.ButsDAO import *
from model import ButsM

class Buits:

    @staticmethod
    def visualiserButs():
        '''
        Visualise tous les buts.
        @retrun: Liste de buts ou message d'erreur
        '''

        try:

            bDAO = ButsDAO()

            bs: list[ButsM.Buts] = bDAO.trouverTout()

            if bs == None:
                return "ERROR"
            
            return bs
        
        except Exception as e:
            print(f"Erreur_ButsC.visualiserButs() ::: {e}")

        return None
    

    @staticmethod
    def visualiserUnBut(idB):

        try:

            bDAO = ButsDAO()

            b: ButsM.Buts = bDAO.trouverUn(idB)

            if b == None:
                return "ERROR"
            
            return b
        
        except Exception as e:
            print(f"Erreur_ButsC.visualiserUnBut() ::: {e}")

        return None
    @staticmethod
    def ajouterBut(idB, nameB):

        try: 

            bDAO = ButsDAO()

            objB = ButsM.Buts()


            objB.setButId(idB)
            obj.

