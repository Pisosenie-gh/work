from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.covid import CovidVaccination, CovidVaccinationStatus
from app.schemas.covid import CovidVaccinationCreate, CovidVaccinationUpdate, CovidVaccinationStatusCreate,CovidVaccinationStatusUpdate


class CRUDCovidVaccination(CRUDBase[CovidVaccination, CovidVaccinationCreate, CovidVaccinationUpdate]):
    def create(self, db: Session, payload: CovidVaccinationCreate):
        db_obj = CovidVaccination(
            VACCINATION_DATE=payload.VACCINATION_DATE,
            VACCINATION_STATUS_ID=payload.VACCINATION_STATUS_ID,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_id(
        self, db: Session, *, id: int
    ) -> List[CovidVaccination]:
        return (
            db.query(self.model)
            .filter(CovidVaccination.ID == id)
            .all()
        )


class CRUDCovidVaccinationStatus(CRUDBase[CovidVaccinationStatus, CovidVaccinationStatusCreate, CovidVaccinationStatusUpdate]):

    def create(self, db: Session, payload: CovidVaccinationStatusCreate):
        db_obj = CovidVaccinationStatus(
            RU=payload.RU,
            KZ=payload.KZ,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_id(
        self, db: Session, *, id: int, skip: int = 0, limit: int = 100
    ) -> List[CovidVaccinationStatus]:
        return (
            db.query(self.model)
            .filter(CovidVaccinationStatus.ID == id)
            .offset(skip)
            .limit(limit)
            .all()
        )

covid = CRUDCovidVaccination(CovidVaccination)
covidstatus = CRUDCovidVaccinationStatus(CovidVaccination)