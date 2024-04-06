from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func

#Informing SQL Alchemy that the table exists by making the sub class Check Ins
class CheckIns(Base):
    __tablename__ = "check_ins"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True) #Column for Id
    created_at = Column(DateTime, nullable=False, default=func.now()) #Column for date
    attendee_id = Column(String, nullable=False) #Column for attendeeId

    def __repr__(self):
        return f"[Check_Ins id={self.id}, created_at={self.created_at}, attendeeId={self.attendee_id}"