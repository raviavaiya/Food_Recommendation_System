from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Home():
    return {"message": "Welcome to the Food Recommendation System API"}

@app.get("/recommendations")
def get_recommendations():
    # Placeholder for recommendations logic
    return {"recommendations": ["Pizza", "Burger", "Pasta"]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)