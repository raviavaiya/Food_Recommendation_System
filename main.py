from fastapi import FastAPI,Request
import mysql.connector
import pandas as pd
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
app = FastAPI()
templates = Jinja2Templates(directory="static")

# Function to fetch all products
def get_all_products():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="food_system"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tbl_product")
    data = cursor.fetchall()
    conn.close()

    # Create DataFrame
    df = pd.DataFrame(data, columns=['id', 'p_name', 'p_type', 'protin', 'fat', 'carbos', 'description'])

    # Convert to list of dicts for JSON response
    return df.to_dict(orient="records")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    products = get_all_products()
    return templates.TemplateResponse("index.html", {"request": request, "products": products})

@app.get("/recommendations")
def get_recommendations():
    # Placeholder for recommendations logic
    return {"recommendations": ["Pizza", "Burger", "Pasta"]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)