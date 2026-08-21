from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get("/")
def greet():
    return "Hello World"

product1 = Product(name = "Laptop", id=1, description="Gaming laptop",
                   price=100, quantity=5)
product2 = Product(name = "Mobile", id=2, description="Usage Mobiles",
                   price=50, quantity=10)
@app.get("/products")
def products():
    return product1, product2