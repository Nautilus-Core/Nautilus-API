from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

date = datetime.now().strftime("%Y-%m-%d")

@router.get("/latest")
async def get_latest_data():
    return {
        "data": [
            {
                "temperature": 15.2,
                "salinity": 35.0,
                "conductivity": 3.5,
                "oxygen": 7.0,
                "timestamp": date,
                "geo": {
                    "lat": 37.7749,
                    "lon": -122.4194
                }
            },
            {
                "temperature": 15.1,
                "salinity": 35.1,
                "conductivity": 3.6,
                "oxygen": 7.1,
                "timestamp": date,
                "geo": {
                    "lat": 37.7749,
                    "lon": -122.4194
                }
            }
            
        ]
    }