from fastapi import FastAPI, Request
import logging
from routes.automations_routes import router as automation_router
import json

# Set up the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "alive"}
app.include_router(automation_router, prefix="/automation")



    

        
