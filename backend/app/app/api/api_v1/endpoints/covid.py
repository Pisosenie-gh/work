from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.CovidVaccinationWithStatus])
def read_covid(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    id: int = None) -> Any:

    if id is not None:
        CovidVaccinationWithStatus = crud.covid.get_multi_by_id(db, id=id)
    else:
        CovidVaccinationWithStatus = crud.covid.get_multi(db, skip=skip, limit=limit)

    return CovidVaccinationWithStatus








@router.get("/{id}", response_model=schemas.CovidVaccinationWithStatus)
def read_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,

) -> Any:
    """
    Get item by ID.
    """
    item = crud.covid.get_multi_by_id(db=db, id=id)

    return item


@router.get("/get/status", response_model=List[schemas.CovidVaccinationStatusUpdate])
def get_all(*, db: Session = Depends(deps.get_db)):
    return db.query(models.CovidVaccinationStatus).all()

@router.post("/status/create", response_model=schemas.CovidVaccinationStatusCreate)
def create_status(*, db: Session = Depends(deps.get_db), payload: schemas.CovidVaccinationStatusCreate):
    note = crud.covidstatus.create(db=db, payload=payload)
    return note

@router.post("/covid/create", response_model=schemas.CovidVaccinationCreate)
def create_status(*, db: Session = Depends(deps.get_db), payload: schemas.CovidVaccinationCreate):
    note = crud.covid.create(db=db, payload=payload)
    return note
