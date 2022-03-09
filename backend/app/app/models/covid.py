from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, VARCHAR, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base



class CovidVaccinationStatus(Base):
    __tablename__ = 'covid_status'
    ID = Column(Integer, primary_key=True, index=True)
    RU = Column(VARCHAR(255))
    KZ = Column(VARCHAR(255))
    parent = relationship("CovidVaccination", backref='covid_status', )

class CovidVaccination(Base):
    __tablename__ = 'covid_vacination'
    ID = Colum n(Integer, primary_key=True, index=True)
    VACCINATION_DATE =(DateTime)
    VACCINATION_STATUS_ID = Column(Integer, ForeignKey('covid_status.ID'))
    NAME = relationship("CovidVaccinationStatus", backref='init',viewonly = True)



