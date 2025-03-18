from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from ..core.database_connection import get_db
from ..interfaces.models import WeatherData

router = APIRouter()

# Route to get current weather data
# Query parameters: lat, lon
@router.get("/current")
async def get_current(lat: float = Query(...), lon: float = Query(...), db: Session = Depends(get_db)):
    weather_data = db.query(WeatherData).filter(WeatherData.location.ST_Within(f'POINT({lat} {lon})')).first()
    return {"data": weather_data}

# Route to get forecast data
# Query parameters: lat, lon
@router.get("/forecast")
async def get_forecast(lat: float = Query(...), lon: float = Query(...), db: Session = Depends(get_db)):
    weather_data = db.query(WeatherData).filter(WeatherData.location.ST_Within(f'POINT({lat} {lon})')).first()
    return {"data": weather_data}

# Route to get historical data
# Query parameters: lat, lon
@router.get("/history")
async def get_history(lat: float = Query(...), lon: float = Query(...), db: Session = Depends(get_db)):
    weather_data = db.query(WeatherData).filter(WeatherData.location.ST_Within(f'POINT({lat} {lon})')).first()
    return {"data": weather_data}

# Route to get alerts data
# Query parameters: lat, lon
@router.get("/alerts")
async def get_alerts(lat: float = Query(...), lon: float = Query(...), db: Session = Depends(get_db)):
    alerts_data = db.query(WeatherData).filter(WeatherData.location.ST_Within(f'POINT({lat} {lon})')).first()
    return {"data": alerts_data}

# Route to get the air quality
# Query parameters: lat, lon
@router.get("/air_quality")
async def get_air_quality(lat: float = Query(...), lon: float = Query(...), db: Session = Depends(get_db)):
    air_quality_data = db.query(WeatherData).filter(WeatherData.location.ST_Within(f'POINT({lat} {lon})')).first()
    return {"data": air_quality_data}