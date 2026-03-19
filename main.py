from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Printanan API Backend")

class Order(BaseModel):
    id: Optional[int] = None
    client_name: str
    print_type: str
    num_pages: int
    notes: Optional[str] = None
    status: str = "pending"

class StatusUpdate(BaseModel):
    status: str

orders_db = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Printanan API"}

@app.get("/orders", response_model=List[Order])
def get_orders():
    return orders_db

@app.post("/orders", response_model=Order, status_code=201)
def create_order(order: Order):
    order.id = len(orders_db) + 1
    orders_db.append(order)
    return order

@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int):
    for order in orders_db:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.put("/orders/{order_id}", response_model=Order)
def update_order(order_id: int, status_update: StatusUpdate):
    for order in orders_db:
        if order.id == order_id:
            order.status = status_update.status
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.get("/orders/status/{status}", response_model=List[Order])
def get_orders_by_status(status: str):
    return [order for order in orders_db if order.status.lower() == status.lower()]

@app.get("/orders/type/{print_type}", response_model=List[Order])
def get_orders_by_type(print_type: str):
    return [order for order in orders_db if order.print_type.lower() == print_type.lower()]

@app.delete("/orders/{order_id}", status_code=204)
def delete_order(order_id: int):
    for i, order in enumerate(orders_db):
        if order.id == order_id:
            del orders_db[i]
            return Response(status_code=204)
    raise HTTPException(status_code=404, detail="Order not found")
