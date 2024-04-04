from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer

#Informing SQL Alchemy that the table exists by making the sub class Events
class Events(Base):
    __tablename__ = "events"

    id = Column(String, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    details = Column(String)
    slug = Column(String, nullable=False)
    maximum_attendees = Column(Integer)

