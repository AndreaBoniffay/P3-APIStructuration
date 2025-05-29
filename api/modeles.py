from sqlalchemy import (
    create_engine, Column, Integer, String, DateTime, Text,
    ForeignKey, PrimaryKeyConstraint
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Table: patients
class Patient(Base):
    __tablename__ = 'patients'

    row_id = Column(Integer)
    subject_id = Column(Integer, primary_key=True)
    gender = Column(Text)
    dob = Column(DateTime)
    dod = Column(DateTime)
    dod_hosp = Column(DateTime)
    dod_ssn = Column(DateTime)
    expire_flag = Column(Integer)

    # Relations
    admissions = relationship('Admission', back_populates='patient')
    diagnoses_icd = relationship('DiagnosisICD', back_populates='patient')


# Table: d_icd_diagnoses
class DICDDiagnosis(Base):
    __tablename__ = 'd_icd_diagnoses'

    row_id = Column(Integer)
    icd9_code = Column(Text, primary_key=True)
    short_title = Column(Text)
    long_title = Column(Text)

    # Relations
    diagnoses_icd = relationship('DiagnosisICD', back_populates='diagnosis')


# Table: admissions
class Admission(Base):
    __tablename__ = 'admissions'

    row_id = Column(Integer)
    subject_id = Column(Integer, ForeignKey('patients.subject_id'))
    hadm_id = Column(Integer, primary_key=True)
    admittime = Column(DateTime)
    dischtime = Column(DateTime)
    deathtime = Column(DateTime)
    admission_type = Column(Text)
    admission_location = Column(Text)
    discharge_location = Column(Text)
    insurance = Column(Text)
    language = Column(Text)
    religion = Column(Text)
    marital_status = Column(Text)
    ethnicity = Column(Text)
    edregtime = Column(DateTime)
    edouttime = Column(DateTime)
    diagnosis = Column(Text)
    hospital_expire_flag = Column(Integer)
    has_chartevents_data = Column(Integer)

    # Relations
    patient = relationship('Patient', back_populates='admissions')
    diagnoses_icd = relationship('DiagnosisICD', back_populates='admission')


# Table: diagnoses_icd
class DiagnosisICD(Base):
    __tablename__ = 'diagnoses_icd'

    row_id = Column(Integer)
    subject_id = Column(Integer, ForeignKey('patients.subject_id'))
    hadm_id = Column(Integer, ForeignKey('admissions.hadm_id'))
    seq_num = Column(Integer)
    icd9_code = Column(Text, ForeignKey('d_icd_diagnoses.icd9_code'))

    __table_args__ = (
        PrimaryKeyConstraint('subject_id', 'hadm_id', 'seq_num'),
    )

    # Relations
    patient = relationship('Patient', back_populates='diagnoses_icd')
    admission = relationship('Admission', back_populates='diagnoses_icd')
    diagnosis = relationship('DICDDiagnosis', back_populates='diagnoses_icd')