from dao.ManagersDAO import *
from model import ManagersM

class Mananger:

    @staticmethod
    def visualiserM():

        try:

            manDAO = ManagersDAO()

            mans: list[ManagersM.Managers] = manDAO.trouverTout()

            if mans==None :
                return "ERROR"

            return mans

        except Exception as e:
            print(f'Erreur_ManagersC.visualiserM() ::: {e}')

        return None

    @staticmethod
    def visualiserUnM(idMan):

        try:

            manDAO = ManagersDAO()

            man: ManagersM.Managers = manDAO.trouverUn(idMan)

            if man==None :
                return "ERROR"

            return man

        except Exception as e:
            print(f'Erreur_ManagersC.visualiserUnM() ::: {e}')

        return None


    @staticmethod
    def ajouterUnM(idMan, nomManager, premonManager, equipe, posteManager):

        try:

            manDAO = ManagersDAO()

            objMan = ManagersM.Managers()

            objMan.setManagerId(idMan)
            objMan.setNomManager(nomManager)
            objMan.setPrenomManager(premonManager)
            objMan.setEquipe(equipe)
            objMan.setPosteManager(posteManager)


            man: int = manDAO.insererUn(objMan)

            if man==0:
                return "ERROR"

            return "AJOUT M AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_ManagersC.ajouterUnM() ::: {e}')

        return None

    @staticmethod
    def modifierUnM(idMan, nomManager, premonManager, equipe, posteManager):

        try:

            manDAO = ManagersDAO()
            objMan = ManagersM.Managers()

            # objM.setManagerId(idMan)
            objMan.setNomManager(nomManager)
            objMan.setPrenomManager(premonManager)
            objMan.setEquipe(equipe)
            objMan.setPosteManager(posteManager)

            man: int = manDAO.modifierUn(idMan, objMan)

            if man==0 :
                return "ERROR"

            return "MODIFICATION DE M AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_managersC.modifierUnM() ::: {e}')

        return None

    @staticmethod
    def supprimerUnM(idMan):

        try:

            manDAO = ManagersDAO()

            man: int = manDAO.supprimerUn(idMan)

            if man==0 :
                return "ERROR"

            return "SUPPRESSION M AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_ManagersC.supprimerUnJ() ::: {e}')

        return None