from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

URL_DATABASE = "sqlite:///./Clinical.db"

#création du moteur de base donnée (Core)
engine = create_engine(
URL_DATABASE, connect_args={"check_same_thread": False}
)
#création de la session (ORM)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


### TEST DE CONNECTION ###
if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            print("Connexion à la base de données réussie.")
    except Exception as e:
        print(f"Erreur de connexion : {e}")



Base = declarative_base()

