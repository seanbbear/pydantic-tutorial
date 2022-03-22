from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item

def main():
    # arg parse
    if False:
        # cli
        pass
    else:
        uvicorn.run(app, host="127.0.0.1", port=8080)


if __name__ == "__main__":
    main()
