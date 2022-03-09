from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from pydantic.types import  List
from typing import Optional
from pydantic.datetime_parse import parse_datetime


class StringDate(datetime):
    @classmethod
    def __get_validators__(cls):
        yield parse_datetime
        yield cls.validate

    @classmethod
    def validate(cls, v: datetime):
        return v.isoformat()





class CovidVaccinationStatusBase(BaseModel):
    RU: str
    KZ: str


class CovidVaccinationStatusCreate(CovidVaccinationStatusBase):
    RU: str
    KZ: str

    class Config:
        orm_mode = True


class CovidVaccinationStatusUpdate(CovidVaccinationStatusBase):
    ID: str
    pass
    class Config:
        orm_mode = True

class CovidVaccinationStatusInDBBase(CovidVaccinationStatusBase):

    pass

    class Config:
        orm_mode = True

class CovidVaccinationStatus(CovidVaccinationStatusInDBBase):

    pass
    class Config:
        orm_mode = True
class CovidVaccinationStatusInDB(CovidVaccinationStatusInDBBase):

    pass

########################################

class CovidVaccinationBase(BaseModel):

    VACCINATION_DATE: Optional[datetime]


    class Config:
        orm_mode = True
class CovidVaccinationCreate(CovidVaccinationBase):

    VACCINATION_STATUS_ID: int


    class Config:
        orm_mode = True

class CovidVaccinationUpdate(CovidVaccinationBase):

    pass


class CovidVaccinationInDBBase(CovidVaccinationBase):

    pass

    class Config:
        orm_mode = True


class CovidVaccination(CovidVaccinationInDBBase):

    pass


class CovidVaccinationInDB(CovidVaccinationInDBBase):

    pass

class CovidVaccinationWithStatus(CovidVaccinationInDBBase):

    ID: int
    NAME: CovidVaccinationStatus

    class Config:
        orm_mode = True
