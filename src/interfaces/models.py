from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Integer, String, DateTime, Boolean, ForeignKey
from geoalchemy2 import Geography
from datetime import datetime

Base = declarative_base()

class OceanData(Base):
    __tablename__ = 'ocean'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    location = Column(Geography(geometry_type="POINT", srid=4326), nullable=False)
    altitude = Column(Float)
    temperature = Column(Float)
    wave_height = Column(Float)
    wave_period = Column(Float)
    salinity = Column(Float)
    ph = Column(Float)
    oxygen = Column(Float)
    chlorophyll = Column(Float)
    sea_level = Column(Float)

class WeatherData(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    location = Column(Geography(geometry_type="POINT", srid=4326), nullable=False)
    air_temperature = Column(Float)
    humidity = Column(Float)
    wind_speed = Column(Float)
    wind_direction = Column(Float)
    precipitation = Column(Float)
    pressure = Column(Float)
    cloud_cover = Column(Float)