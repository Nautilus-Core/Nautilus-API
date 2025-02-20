from fastapi import APIRouter, Query
from datetime import datetime

router = APIRouter()

# Get the current date
date = datetime.now().strftime("%Y-%m-%d")

# Route to get forecast data
# Query parameters: lat, lon
@router.get("/current")
async def get_current(lat: float = Query(...), lon: float = Query(...)):
    return {
        "data": {
            "temperature": 15.0,
            "salinity": 35.0,
            "sea_level": 0.0,
            "waves": 0.0,
            "timestamp": date,
            "geo": {
                "lat": lat,
                "lon": lon
            }
        }
   }

# Route to get historical data
# Query parameters: lat, lon
@router.get("/forecast")
async def get_forecast(lat: float = Query(...), lon: float = Query(...)):
    return {
        "data": {
            "temperature": 15.0,
            "salinity": 35.0,
            "sea_level": 0.0,
            "waves": 0.0,
            "timestamp": date,
            "geo": {
                "lat": lat,
                "lon": lon
            }
        }
    }

# Route to get historical data
# Query parameters: lat, lon
@router.get("/history")
async def get_history(lat: float = Query(...), lon: float = Query(...)):
    return {
        "data": {
            "temperature": 15.0,
            "salinity": 35.0,
            "sea_level": 0.0,
            "waves": 0.0,
            "timestamp": date,
            "geo": {
                "lat": lat,
                "lon": lon
            }
        }
    }

# Route to get alerts data
# Query parameters: lat, lon
@router.get("/alerts")
async def get_alerts(lat: float = Query(...), lon: float = Query(...)):
    return {
        "data": {
            "alerts": 0,
            "timestamp": date,
            "geo": {
                "lat": lat,
                "lon": lon
            }
        }
    }

# Route to get the air quality
# Query parameters: lat, lon

@router.get("/air_quality")
async def get_air_quality(lat: float = Query(...), lon: float = Query(...)):
    return {
        "data": {
            "air_quality": 0,
            "timestamp": date,
            "geo": {
                "lat": lat,
                "lon": lon
            }
        }
    }