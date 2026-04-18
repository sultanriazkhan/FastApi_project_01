from fastapi import FastAPI, Request
from data_01 import products
app=FastAPI()
@app.get("/")
def Home():
    return {"Home page pe aya hai ladle!"}
@app.get("/products")
def get_the_products_list():
    return products
@app.get("/products/{product_id}")
def get_product_via_id(product_id:int):
    for product in products:
        if product["id"]==product_id:
            return product
    return {"Error":"Product not found!"}
@app.get("/greet")
def greet_user(name:str):
    return {"message":f"Hello {name}, welcome to FastAPI!"}
@app.get("/search")
def dummy_search(request:Request):
    print (request)