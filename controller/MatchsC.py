from dao.MatchsDAO import *
from model import MatchsM

class Matchs:

    @staticmethod
    def visualiserMatch():

        try:

            matchDAO = MatchsDAO()

            matchs: list[MatchsM.Matchs] = matchDAO.trouverTout()

            if matchs==None :
                return "ERROR"

            return matchs

        except Exception as e:
            print(f'Erreur_MatchsC.visualiserMatch() ::: {e}')

        return None

    @staticmethod
    def visualiserUnMatch(idMatch):

        try:

            matchDAO = MatchsDAO()

            match: MatchsM.Matchs = matchDAO.trouverUn(idMatch)

            if match==None :
                return "ERROR"

            return match

        except Exception as e:
            print(f'Erreur_MatchsC.visualiserUnMatch() ::: {e}')

        return None


    @staticmethod
    def ajouterUnMatch(idMatch, date, stade, resultat):

        try:

            matchDAO = MatchsDAO()

            objMatch = MatchsM.Matchs()

            objMatch.setMatchId(idMatch)
            objMatch.setDate(date)
            objMatch.setStade(stade)
            objMatch.setResultat(resultat)

            match: int = matchDAO.insererUn(objMatch)

            if match==0:
                return "ERROR"

            return "AJOUT Match AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_MatchsC.ajouterUnMatch() ::: {e}')

        return None

    @staticmethod
    def modifierUnMatch(idMatch, date, stade, resultat):

        try:

            matchDAO = MatchsDAO()
            objMatch = MatchsM.Matchs()

            # objJ.setJoueurId(idJ)
            objMatch.setDate(date)
            objMatch.setStade(stade)
            objMatch.setResultat(resultat)

            match: int = matchDAO.modifierUn(idMatch, objMatch)

            if match==0 :
                return "ERROR"

            return "MODIFICATION DE Match AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_MatchC.modifierUnMatch() ::: {e}')

        return None

    @staticmethod
    def supprimerUnJ(idMatch):

        try:

            matchDAO = MatchsDAO()

            match: int = matchDAO.supprimerUn(idMatch)

            if match==0 :
                return "ERROR"

            return "SUPPRESSION Match AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_MatchsC.supprimerUnMatch() ::: {e}')

        return None