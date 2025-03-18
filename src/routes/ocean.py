from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from geoalchemy2.elements import WKTElement
from geoalchemy2.shape import to_shape
from ..core.database_connection import get_db
from ..interfaces.models import OceanData

router = APIRouter()

# Get the current date
date = datetime.now().strftime("%Y-%m-%d")

# Route to get temperature data
# Query parameters: lat, lon
@router.get("/temperature")
async def get_temperature(lat: float = Query(...), lon: float = Query(...), db: Session = Depends(get_db)):
    point = WKTElement(f'POINT({lon} {lat})', srid=4326)
    data = db.query(OceanData).filter(OceanData.location.ST_DWithin(point, 0)).first()
    return {
        "data": {
            "temperature": data.temperature if data else None,
            "timestamp": date,
            "geo": {
                "lat": lat,
                "lon": lon
            }
        }
    }

# Route to get salinity data
# Query parameters: lat, lon
@router.get("/salinity")
async def get_salinity(lat: float = Query(...), lon: float = Query(...), db: Session = Depends(get_db)):
    point = WKTElement(f'POINT({lon} {lat})', srid=4326)
    data = db.query(OceanData).filter(OceanData.location.ST_DWithin(point, 0)).first()
    return {
        "data": {
            "salinity": data.salinity if data else None,
            "timestamp": date,
            "geo": {
                "lat": lat,
                "lon": lon
            }
        }
    }

# Route to get sea level data
# Query parameters: lat, lon
@router.get("/sea_level")
async def get_sea_level(lat: float = Query(...), lon: float = Query(...), db: Session = Depends(get_db)):
    point = WKTElement(f'POINT({lon} {lat})', srid=4326)
    data = db.query(OceanData).filter(OceanData.location.ST_DWithin(point, 0)).first()
    return {
        "data": {
            "sea_level": data.sea_level if data else None,
            "timestamp": date,
            "geo": {
                "lat": lat,
                "lon": lon
            }
        }
    }

# Route to get waves data
# Query parameters: lat, lon
@router.get("/waves")
async def get_waves(lat: float = Query(...), lon: float = Query(...), db: Session = Depends(get_db)):
    point = WKTElement(f'POINT({lon} {lat})', srid=4326)
    data = db.query(OceanData).filter(OceanData.location.ST_DWithin(point, 0)).first()
    return {
        "data": {
            "waves": data.wave_height if data else None,
            "timestamp": date,
            "geo": {
                "lat": lat,
                "lon": lon
            }
        }
    }

# Route to get currents data
# Query parameters: lat, lon
@router.get("/currents")
async def get_currents(lat: float = Query(...), lon: float = Query(...), db: Session = Depends(get_db)):
    point = WKTElement(f'POINT({lon} {lat})', srid=4326)
    data = db.query(OceanData).filter(OceanData.location.ST_DWithin(point, 0)).first()
    return {
        "data": {
            "currents": data.currents if data else None,
            "timestamp": date,
            "geo": {
                "lat": lat,
                "lon": lon
            }
        }
    }

# Route to get chlorophyll data
# Query parameters: lat, lon
@router.get("/chlorophyll")
async def get_chlorophyll(lat: float = Query(...), lon: float = Query(...), db: Session = Depends(get_db)):
    point = WKTElement(f'POINT({lon} {lat})', srid=4326)
    data = db.query(OceanData).filter(OceanData.location.ST_DWithin(point, 0)).first()
    return {
        "data": {
            "chlorophyll": data.chlorophyll if data else None,
            "timestamp": date,
            "geo": {
                "lat": lat,
                "lon": lon
            }
        }
    }

# Route to get all the ocean data
@router.get("/all_ocean_data")
async def get_all_ocean_data(lat: float = Query(...), lon: float = Query(...), db: Session = Depends(get_db)):
    point = WKTElement(f'POINT({lon} {lat})', srid=4326)
    data = db.query(OceanData).filter(OceanData.location.ST_DWithin(point, 0)).first()
    return {
        "data": {
            "temperature": data.temperature if data else None,
            "salinity": data.salinity if data else None,
            "sea_level": data.sea_level if data else None,
            "waves": data.wave_height if data else None,
            "currents": data.currents if data else None,
            "chlorophyll": data.chlorophyll if data else None,
            "timestamp": date,
            "geo": {
                "lat": lat,
                "lon": lon
            }
        }
    }