from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Resume(Base):
    __tablename__ = 'resumes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String)
    content = Column(Text)
    personal_info = relationship("PersonalInfo", uselist=False, back_populates="resume")
    education = relationship("Education", back_populates="resume")
    work_experience = relationship("WorkExperience", back_populates="resume")
    roles_responsibilities = relationship("RolesResponsibilities", back_populates="resume")

class PersonalInfo(Base):
    __tablename__ = 'personal_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    resume_id = Column(Integer, ForeignKey('resumes.id'))
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    resume = relationship("Resume", back_populates="personal_info")

class Education(Base):
    __tablename__ = 'education'
    id = Column(Integer, primary_key=True, autoincrement=True)
    resume_id = Column(Integer, ForeignKey('resumes.id'))
    degree = Column(String)
    institution = Column(String)
    certification = Column(String)
    resume = relationship("Resume", back_populates="education")

class WorkExperience(Base):
    __tablename__ = 'work_experience'
    id = Column(Integer, primary_key=True, autoincrement=True)
    resume_id = Column(Integer, ForeignKey('resumes.id'))
    job_title = Column(String)
    company = Column(String)
    duration = Column(String)
    resume = relationship("Resume", back_populates="work_experience")

class RolesResponsibilities(Base):
    __tablename__ = 'roles_responsibilities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    resume_id = Column(Integer, ForeignKey('resumes.id'))
    role = Column(String)
    responsibilities = Column(Text)
    resume = relationship("Resume", back_populates="roles_responsibilities")

# Setup the database
engine = create_engine('sqlite:///resume_analyzer.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
