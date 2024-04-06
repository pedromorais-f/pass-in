from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func

#Informing SQL Alchemy that the table exists by making the sub class Events
class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True) #Column for Id
    created_at = Column(DateTime, nullable=False, default=func.now()) #Column for title
    attendeeId = Column(String, nullable=False) #Column for details

    def __repr__(self):
        return f"[Check_Ins id={self.id}, created_at={self.created_at}, attendeeId={self.attendeeId}"