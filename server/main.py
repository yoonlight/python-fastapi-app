from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from server.database import get_database

app = FastAPI()

dbname = get_database()
collection_name = dbname["user_1_items"]

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    item = Item(**collection_name.find_one({"item_id": item_id}))
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    result = item.dict()
    result["item_id"] = item_id
    collection_name.insert_one(result)
    return {"item_name": item.name, "item_id": item_id}