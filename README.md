# 🌊Nautilus API

Nautilus API is an open-source project aimed at providing data and tools for oceanic research. Built with FastAPI, it offers a structured and scalable architecture for handling various research-related data.

## ⚒️Features
- **FastAPI-based**: High-performance and easy-to-use Python web framework.
- **Modular Routes**: Organized routes for better maintainability.
- **Static Files Support**: Properly serves static assets like `favicon.ico`.
- **Versioning**: Ensures API longevity and compatibility.

## ☘️Installation
### Requirements
- Python 3.10+
- FastAPI
- Uvicorn

### 💻Setup
```bash
# Clone the repository
git clone https://github.com/Nautilus/Nautilus.git
cd Nautilus-API

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the API
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

## Project Structure
```
Nautilus-API/
│── src/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── routes/
│   │   ├── general.py
│   │   ├── data.py
│   ├── services/
│   ├── main.py
│── static/
│   ├── favicon.ico
│── .gitignore
│── LICENSE
│── README.md
│── requirements.txt
```

## API Endpoints
### 🛰️General
- `GET /status` - Check API status
- `GET /health`- Check API Health
- `GET /info` - Check API info

### ☀️ Weather
- `GET weather/current` - Retrieve the current weather
- `GET weather/forecast` - Retrieve the forecast
- `GET weather/history` - Retrieve the weather history
- `GET weather/alerts` - Retrieve any alerts on the area
- `GET weather/air_quality` - Retrieve the air quality

### 🌊 Ocean
- `GET ocean/temperature` - Retrieve sea temperature
- `GET ocean/salinity` - Retrieve sea salinity
- `GET ocean/sea_level` - Retrieve sea level
- `GET ocean/currents` - Retrieve currents
- `GET ocean/chlorophyll` - Retrieve clorophyll
- `GET ocean/all_ocean_data` - Retrieve all the ocean data at the same time

## 📜License
This project is licensed under the **Apache License 2.0** - see the [LICENSE](LICENSE) file for details.

## 🧸Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## 📞Contact
For inquiries or collaboration, reach out via GitHub Issues.

