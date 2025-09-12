from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Calorie Tracker API"}

@app.get("/api/foods")
def get_foods():
    return {"foods": ["apple", "banana", "chicken"]}