from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Sequence
from sqlalchemy.orm import relationship
from base import BaseModel

class Unicoron(BaseModel):
    __tablename__ = 'unicorn'

    id = Column(Integer, Sequence('unicorn_seq'), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    color = Column(String(80))
    created = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, name, color):
        self.name = name
        self.color = color


class Locations(BaseModel):
    __tablename__ = 'location'

    id = Column(Integer, Sequence('location_seq'), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    created = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, name):
        self.name = name

class UnicornLocations(BaseModel):
    __tablename__ = 'unicornlocations'
    unicorn_id = Column(Integer, ForeignKey(Unicorn.id))
    location_id = Column(Integer, ForeignKey(Locations.id))

    def __init__(self, unicorn_id, location_id):
        self.unicorn_id = unicorn_id
        self.location_id = location_id
        
