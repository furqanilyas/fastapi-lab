from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def greet():
    return "Hello World"

@app.get("/products")
def products():
    return "Gimme all products"