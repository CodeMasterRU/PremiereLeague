import psycopg2  # pip install psycopg2-binary
import yaml # pip install PyYAML

class ConnexionBD:

    def __init__(self):
        self.cnx = None
        self.params = None

    def getConnexion(self):
        try:
            print("- class connexionBD() is running ... \n\n")
            print("- config/Config.yml is loading ...")

            # get file and data
            with open("./config/Config.yaml", "r") as fic:
                config = yaml.safe_load(fic)
            db = config["database_name"]
            host = config["host"]
            port = config["port"]
            usr = config["user"]
            pwd = config["pwd"]

            self.cnx = psycopg2.connect(database=db,
                                  host=host,
                                  port=port,
                                  user=usr,
                                  password=pwd
                                  )
            print('Connexion réussi')
            return self.cnx
        except Exception as e:
            print(f"Erreur-CONNECTION ::: {e}")
        return self.cnx