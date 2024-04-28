from typing import List
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .db import SessionLocal
from .models import Booking, Member, Facility
from .schemas import BookingGet, UserGet, FacilityGet

app = FastAPI()


def get_session():
    with SessionLocal() as session:
        return session


@app.get("/user/all", response_model=List[UserGet])
def get_all_users(limit: int = 10, db: Session = Depends(get_session)):
    return db.query(Member).limit(limit).all()


@app.get("/facility/all", response_model=List[FacilityGet])
def get_all_facilities(limit: int = 1, db: Session = Depends(get_session)):
    return db.query(Facility).limit(limit).all()


@app.get("/booking/all", response_model=List[BookingGet])
def get_all_bookings(limit: int = 10, db: Session = Depends(get_session)):
    return db.query(Booking).limit(limit).all()