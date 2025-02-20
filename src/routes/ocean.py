from fastapi import APIRouter, Query
from datetime import datetime

router = APIRouter()

# Get the current date
date = datetime.now().strftime("%Y-%m-%d")


# Route to get temperature data
# Query parameters: lat, lon
@router.get("/temperature")
async def get_temperature(lat: float = Query(...), lon: float = Query(...)):
    return {
        "data": {
            "temperature": 15.0,
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
async def get_salinity(lat: float = Query(...), lon: float = Query(...)):
    return {
        "data": {
            "salinity": 35.0,
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
async def get_sea_level(lat: float = Query(...), lon: float = Query(...)):
    return {
        "data": {
            "sea_level": 0.0,
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
async def get_waves(lat: float = Query(...), lon: float = Query(...)):
    return {
        "data": {
            "waves": 0.0,
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
async def get_currents(lat: float = Query(...), lon: float = Query(...)):
    return {
        "data": {
            "currents": 0.0,
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
async def get_chlorophyll(lat: float = Query(...), lon: float = Query(...)):
    return {
        "data": {
            "chlorophyll": 0.0,
            "timestamp": date,
            "geo": {
            "lat": lat,
            "lon": lon
            }
        }
    }


# Route to get all the ocean data
@router.get("/all_ocean_data")
async def get_all_ocean_data(lat: float = Query(...), lon: float = Query(...)):
    return {
        "data": {
            "temperature": 15.0,
            "salinity": 35.0,
            "sea_level": 0.0,
            "waves": 0.0,
            "currents": 0.0,
            "chlorophyll": 0.0,
            "timestamp": date,
            "geo": {
            "lat": lat,
            "lon": lon
            }
        }
    }