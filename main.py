from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title = "SOL-Mehrab_API", version = "2.0.2.6")


# Pydantic model - the data shape
class iteam(BaseModel):
    name: str
    price: float
    in_stock: bool = True


# get [read data]

@app.get("/iteams/{item_id}")

async def get_iteam(iteam_id: str, q: str | None = None):
    return {"iteam_id": iteam_id, "query": q}

# post [receive + validate]
@app.post("/items/", status_code = 201)

async def create_item(item: iteam):
    return item