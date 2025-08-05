from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


class LocationUpdate(BaseModel):
    bus_id : str
    latitude: float
    longitude: float
    timestamp: datetime



app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI! here"}



# Endpoint to update bus location  - tested using swagger UI
# Endpoint: TestSuccessfull 
@app.post("/update_location")
def update_location(data: LocationUpdate):
    #backend logic to update the bus location in the database would go here
    # For now, we will just print the data to the console
    print(f"Received location update for Bus_id : {data.bus_id} \nlatitude: {data.latitude}, \nlongitude: {data.longitude}, \ntimestamp: {data.timestamp}")
    return {"status": "Location updated", "bus": data.bus_id}

