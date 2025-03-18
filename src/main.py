from typing import Union
from fastapi import FastAPI
from .core.config import config

from .routes import router as main_router

app = FastAPI(
    title=config.PROJECT_NAME,
    description=config.PROJECT_DESC,
    version=config.VERSION
)

app.include_router(main_router, prefix=config.API_PREFIX)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )

