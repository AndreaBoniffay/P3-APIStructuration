# From MIMIC .csv to Structured database
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-0868AC?style=flat&logo=sqlalchemy&logoColor=white)
![Render](https://img.shields.io/badge/Render-000000?style=flat&logo=render&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)


##  Description

Ce projet vise à structurer et intégrer des données issues de fichiers CSV dans une base de données relationnelle.

![image](https://github.com/user-attachments/assets/77a25c1d-5aa4-4f9a-9d5b-548a7db2ae01)


- Un espace Notion récapitulant chacune des étapes du projet sera prochainement disponible ici : [👉 lien bientot dispo](https://andreaboniffay.github.io)  

Une API est développée avec FastAPI, et permet d’interagir avec la base de données SQLite `Clinical.db`. Seules les tables concernant les patients, leurs admissions ainsi que les diagnostics ICD et D ICD y sont renseignés.

##  Dataset

Pour ce projet, nous utilisons la base de données : *MIMIC-III Clinical Database Demo* disponibles sur physionet.
- **URL :** [🔗 MIMIC III Demo csv files](https://physionet.org/content/mimiciii-demo/1.4/)  
- **Référence :** [📖 Johnson, A., Pollard, T., Shen, L. et al. MIMIC-III, a freely accessible critical care database. Sci Data 3, 160035 (2016).](https://www.nature.com/articles/sdata201635)



Fonctionnalités principales de l'API
---------------------------

- Récupérer le nombre total de patients.
- Lister les patients avec filtres optionnels (genre, date de naissance).
- Obtenir les informations détaillées d’un patient par ID.
- Accéder aux codes ICD9 avec recherche par code ou titre.
- Lister les admissions avec différents critères de filtrage.
- Récupérer les admissions d’un patient donné.
- Lister les diagnostics ICD par admission avec filtres.


Structure du projet
-------------------

- `database.py` : configuration de la connexion à la base SQLite via SQLAlchemy.
- `modeles.py` : définition des modèles ORM correspondant aux tables de la base de données.
- `main.py` : définition des routes API FastAPI et logique métier.
- `requirements.txt` : dépendances nécessaires pour faire fonctionner l’API.

Installation & utilisation locale
--------------------------------

1. Cloner le dépôt :  
   ```powershell
   git clone https://github.com/AndreaBoniffay/P3-APIStructuration
   cd api
2. Faire tourner en local :
   ```powershell
   uvicorn main:app --reload

Documentation interactive:   
FastAPI génère automatiquement la documentation Swagger à l’URL : "http://127.0.0.1:8000/docs"

![image](https://github.com/user-attachments/assets/b0137604-705a-4b28-914f-985d3efe215b)

# Déploiement
Cette API est déployée sur Render.com et accessible publiquement juste [ici ✨](https://physionet.org/content/mimiciii-demo/1.4/) 

# Exemple d’appels API
Nombre total de patients :  
`GET /total_patients`

Liste des patients, par exemple uniquement les femmes nées le 1990-01-01 :  
`GET /patients?gender=F&dob=1990-01-01T00:00:00`

Détails d’un patient :  
`GET /patient?id=12345`

Codes ICD9 filtrés par titre :  
`GET /icd?long_title=diabetes`

Admissions d’un patient :  
`GET /patient_admissions?id=12345`

##  Licence

Ce projet est sous licence MIT - voir le fichier [📄 LICENSE](LICENSE) pour plus de détails.

##  Contact

[📩 Andréa Boniffay](https://andreaboniffay.github.io) - N'hésitez pas ;) 
