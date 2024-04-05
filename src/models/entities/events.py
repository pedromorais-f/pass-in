from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer

#Informing SQL Alchemy that the table exists by making the sub class Events
class Events(Base):
    __tablename__ = "events"

    id = Column(String, nullable=False, primary_key=True) #Column for Id
    title = Column(String, nullable=False) #Column for title
    details = Column(String) #Column for details
    slug = Column(String, nullable=False) #Column for slug
    maximum_attendees = Column(Integer) #Column for maximun attendees

