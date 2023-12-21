from dao.EquipesDAO import *
from model import EquipesM

class Equipes:

    @staticmethod
    def visualiserEquipes():

        try:

            eDAO = EquipesDAO()

            eqs: list[EquipesM.Equipes] = eDAO.trouverTout()
            print(eqs)
            if eqs==None :
                return "ERROR"

            return eqs

        except Exception as e:
            print(f'Erreur_EquipesC.visualiserEq() ::: {e}')

        return None

    @staticmethod
    def visualiserUneEq(idEQ):

        try:

            eqDAO = EquipesDAO()

            eq: EquipesM.Equipes = eqDAO.trouverUn(idEQ)

            if eq==None :
                return "ERROR"

            return eq

        except Exception as e:
            print(f'Erreur_EquipesC.visualiserUnEq() ::: {e}')

        return None


    @staticmethod
    def ajouterUnEq(equipeID, nomEquipe, manager, joueurs):

        try:

            eqDAO = EquipesDAO()

            objEQ = EquipesM.Equipes()

            objEQ.setEquipeId(equipeID)
            objEQ.setNomDeEquipe(nomEquipe)
            objEQ.setManager(manager)
            objEQ.setJoueurs(joueurs)


            eq: int = eqDAO.insererUn(objEQ)

            if eq==0:
                return "ERROR"

            return "AJOUT Eq AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_EquipesC.ajouterUnEq() ::: {e}')

        return None

    @staticmethod
    def modifierUnEq(equipeID, nomEquipe, manager, joueurs):
        '''
        Modifie un body part.
        @param idBP: ID du body part.
        @param nameBP: Nouveau nom du body part.
        @return: Statut de la modification du body part.
        '''
        try:

            eqDAO = EquipesDAO()
            objEQ = EquipesM.Equipes()

            # objEQ.setEquipeId(equipeID)
            objEQ.setNomDeEquipe(nomEquipe)
            objEQ.setManager(manager)
            objEQ.setJoueurs(joueurs)

            eq: int = eqDAO.modifierUn(equipeID, objEQ)

            if eq==0 :
                return "ERROR"

            return "MODIFICATION DE EQ AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_EquipesC.modifierUnEq() ::: {e}')

        return None

    @staticmethod
    def supprimerUnEq(equipeID):

        try:

            eqDAO = EquipesDAO()

            eq: int = eqDAO.supprimerUn(equipeID)

            if eq==0 :
                return "ERROR"

            return "SUPPRESSION EQ AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_EquipesC.supprimerUnEQ() ::: {e}')

        return None