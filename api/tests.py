# %%
from database import SessionLocal
from modeles import Patient, Admission, DICDDiagnosis, DiagnosisICD
from datetime import datetime


db = SessionLocal()

# %% 
# Tester la récupération de quelques films
patients = db.query(Patient).limit(10).all()
patients

# %% 
for patient in patients:
    print(f"ID : {patient.subject_id}")

else:
    print("No patients found.")



# %%
adms = db.query(Admission).limit(10).all()

for adm in adms:
    print(f"ID : {adm.subject_id}")

else:
    print("No patients found.")



# %%
diags_icd = db.query(DiagnosisICD).limit(10).all()

for x in diags_icd:
    print(f"ID : {x.icd9_code, x.subject_id}")

else:
    print("No diag found.")



# %%
dicd_diags = db.query(DICDDiagnosis).limit(10).all()

for x in dicd_diags:
    print(f"ID : {x.icd9_code}")

else:
    print("No diag found.")

# %%
def get_patients( 
    skip: int = 0, 
    limit: int=100, 
    gender: str = None, 
    dob : datetime = None):

    requete_base = db.query(Patient)

    if gender :
        requete = requete_base.filter(Patient.gender)
    if dob :
        requete = requete_base.filter(Patient.dob)

    return requete.offset(skip).limit(limit).all
# %%
get_patients(gender="M")


