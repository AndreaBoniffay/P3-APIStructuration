from fastapi import FastAPI,Depends
from modeles import Patient, Admission, DICDDiagnosis, DiagnosisICD
from database import SessionLocal
from sqlalchemy.orm import Session

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


### GET request ###
@app.get("/total_patients")
def get_total_patients(session: Session = Depends(get_session)) -> dict:
    total = session.query(Patient).count()
    return {"total_patients": total}
