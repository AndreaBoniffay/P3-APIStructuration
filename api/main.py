from fastapi import FastAPI,Depends
from modeles import Patient, Admission, DICDDiagnosis, DiagnosisICD
from database import SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime

#utiliser ilike pour les pathologies

app = FastAPI(title="Clinical DB API", description="API qui permet l'interaction avec Clinical.db")

### Session ###
def get_session():
      session=SessionLocal()
      try:
        yield session
      finally:
        session.close()

### Test : API en ligne ###
@app.get("/",description="test api")
async def root():
    return("API opérationnelle !")


### GET requests ###

# --- Patients ---

#retourne le nombre total de patients
@app.get("/total_patients")
def get_total_patients(
    session: Session = Depends(get_session)) -> dict:

    total = session.query(Patient).count()
    return {"total_patients": total}


#retourne une liste de patients avec ffiltres optionels

#@param 
# skip : ignore les skip premiers resultats
# limit : affiche une liste de limit patients
# gender : genre 'F' ou 'M' (optionel)
# dob : date of birth yyyy-mm-dd 00:00:00 (optionel)

@app.get("/patients")
def get_patients(
    session: Session = Depends(get_session), 
    skip: int = 0, 
    limit: int=100, 
    gender: str = None, 
    dob : datetime = None):

    requete = session.query(Patient)

    if gender :
        requete = requete.filter(Patient.gender == gender)
    if dob :
        requete = requete.filter(Patient.dob == dob)

    return requete.offset(skip).limit(limit).all()


#retourne le patient sélectionné par son id

#@param 
# id : int

@app.get("/patient")
def get_patient(
    id: int,
    session: Session = Depends(get_session)
    ):

    requete = session.query(Patient)
    patient = requete.filter(Patient.subject_id == id).first()

    return patient


# --- DICDDiagnosis ---

#retourne une liste des codes icd9 et leur titre avec filtres optionels

#@param 
# skip : ignore les skip premiers resultats
# limit : affiche une liste de limit patients
# icd9_code : code icd9 (optionel)
# long_title : titre du code diagnostic icd9 (optionel)

@app.get("/icd")
def get_icd(
    session: Session = Depends(get_session), 
    skip: int = 0, 
    limit: int=100, 
    icd9_code : int = None,
    long_title : str = None
    ):

    requete = session.query(DICDDiagnosis)

    if long_title :
        requete = requete.filter(DICDDiagnosis.long_title.ilike(f"%{long_title}%"))
    if icd9_code :
        requete = requete.filter(DICDDiagnosis.icd9_code == icd9_code)
   
    return requete.offset(skip).limit(limit).all()

# --- Admission ---

#retourne une liste des admissions avec filtres optionels

#@param 
# skip : ignore les skip premiers resultats
# limit : affiche une liste de limit patients
# hadm_id : int id de l'admission (optionel)
# admittime : date de l'admission yyyy-mm-dd 00:00:00 (optionel)
# admission_type : type de l'admission (optionel)
# edouttime : date de decharge du departement d'urgence (optionel)
# diagnosis : diagnostic (optionel)

@app.get("/admissions")
def get_admissions(
    session: Session = Depends(get_session), 
    skip: int = 0, 
    limit: int=100, 
    hadm_id: int = None, 
    admittime : datetime = None,
    admission_type : str = None,
    edouttime : datetime = None,
    diagnosis : str = None):

    requete = session.query(Admission)

    if hadm_id :
        requete = requete.filter(Admission.hadm_id == hadm_id)
    if admittime :
        requete = requete.filter(Admission.admittime == admittime)
    if admission_type :
        requete = requete.filter(Admission.admission_type.ilike(f"%{admission_type}%"))
    if edouttime :
        requete = requete.filter(Admission.edouttime == edouttime)
    if diagnosis :
        requete = requete.filter(Admission.diagnosis.ilike(f"%{diagnosis}%"))

    return requete.offset(skip).limit(limit).all()


#retourne les admissions pour un patient sélectionné par son id

#@param 
# id : int

@app.get("/patient_admissions")
def get_patient_admissions(
    id: int,
    session: Session = Depends(get_session)
    ):

    requete = session.query(Admission)
    admissions = requete.filter(Admission.subject_id == id)

    return admissions.all()

# --- DiagnosisICD ---

#retourne une liste des icd9 par admissions avec filtres optionels

#@param 
# skip : ignore les skip premiers resultats
# limit : affiche une liste de limit patients
# hadm_id : int id de l'admission (optionel)
# subject_id : id du patient (optionel)
# seq_num : ordre de priorité des differents diagnostique pour 1 patient (optionel)
# icd9_code : code icd9 (optionel)


@app.get("/icd_adm")
def get_icd_admissions(
    session: Session = Depends(get_session), 
    skip: int = 0, 
    limit: int=100, 
    subject_id: int = None, 
    hadm_id : int = None,
    seq_num : int = None,
    icd9_code : int = None
    ):

    requete = session.query(DiagnosisICD)

    if hadm_id :
        requete = requete.filter(DiagnosisICD.hadm_id == hadm_id)
    if subject_id :
        requete = requete.filter(DiagnosisICD.subject_id == subject_id)
    if seq_num :
        requete = requete.filter(DiagnosisICD.seq_num == seq_num)
    if icd9_code :
        requete = requete.filter(DiagnosisICD.icd9_code == icd9_code)
   
    return requete.offset(skip).limit(limit).all()