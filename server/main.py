from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel
from bson.objectid import ObjectId

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
def read_item(item_id: str, q: Optional[str] = None):
    item = Item(**collection_name.find_one({"_id": ObjectId(item_id)}))
    return item


@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    collection_name.update_one(
        {"_id": ObjectId(item_id)}, {"$set": item.dict()})
    return "success to update"

@app.post("/items")
def create_item(item: Item):
    result = item.dict()
    collection_name.insert_one(result)
    return "success to create"


@app.get("/items")
def read_items() -> List[Item]:
    items = collection_name.find()
    itemsArr = []
    for item in items:
        itemsArr.append(Item(**item))
    return itemsArr


@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    collection_name.delete_one({"_id": ObjectId(item_id)})
    return "success to delete"
