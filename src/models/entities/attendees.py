from src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func

#Informing SQL Alchemy that the table exists by making the sub class Events
class Attendees(Base):
    __tablename__ = "attendees"

    id = Column(String, nullable=False, primary_key=True) #Column for Id
    name = Column(String, nullable=False) #Column for title
    email = Column(String, nullable=False) #Column for details
    event_id = Column(String, ForeignKey("events_id"), nullable=False) #Column for slug
    created_at = Column(DateTime, nullable=False, default=func.now()) #Column for maximun attendees

    def __repr__(self):
        return f"[Attendees id={self.id}, name={self.name}, email={self.email}], event_id={self.event_id}, created_at={self.created_at}"