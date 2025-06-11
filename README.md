# 🍽️ Food Recommender System

The **Food Recommender System** helps users discover food items based on their dietary preferences such as protein, fat, carbohydrates, and food type (Veg/Non-Veg). It uses nutritional data and filters to personalize recommendations.
<img align="right" alt="Coding" width="600" src="https://github.com/raviavaiya/Food_Recommendation_System/blob/main/image.png">
## 🚀 Features

- Filter food items based on:
  - Protein, Fat, and Carbohydrate levels (in grams)
  - Vegetarian or Non-Vegetarian preference
- Backend built with FastAPI
- Frontend built using HTML/CSS (simple UI)
- Database connected via MySQL
- Real-time food recommendation via REST API

## 🛠️ Technologies Used

- **FastAPI** – Backend API framework
- **HTML/CSS** – Frontend UI
- **MySQL** – Database to store food data
- **Python** – Core programming language
- **JavaScript** – (Optional) For dynamic UI interactions

## 📦 Project Structure

food-recommender/
├── backend/
│ └── main.py # FastAPI backend logic
├── frontend/
│ ├── index.html # UI to display recommendations
│ └── style.css # Optional styling
├── data/
│ └── food_data.sql # SQL dump of food nutrition data
├── README.md



## 🧪 Sample Food Dataset

| Food_Name | F_type  | Ingredients       | Protein (g) | Fat (g) | Carbos (g) |
|-----------|---------|-------------------|-------------|---------|------------|
| Apple     | Fruit   | Apple             | 0.3         | 0.2     | 14         |
| Chicken   | Meat    | Chicken breast    | 31          | 3.6     | 0          |
| Rice      | Grain   | White rice        | 2.7         | 0.3     | 28         |
| Paneer    | Veg     | Cottage cheese    | 18          | 20      | 1.2        |
| Eggs      | Non-Veg | Eggs              | 13          | 11      | 1.1        |

## 🔧 How to Run Locally

### 1. Clone the Repository

git clone https://github.com/raviavaiya/food-recommendation_system.git
cd food-recommendation_system

### 2. Setup MySQL
Create a database and import food_data.sql located in data/ folder.

### 3. Setup and Run FastAPI Backend

cd backend
pip install fastapi uvicorn pymysql
uvicorn main:app --reload

### 4. Open Frontend
Open frontend/index.html in your browser to interact with the recommender system.

## 📈 Future Enhancements

Add image-based UI for food items

Add login/authentication system

Support user feedback and ratings

Use ML models for smart recommendation

## 🙌 Contributing
Feel free to fork this repo and suggest improvements via pull requests!

## Made with ❤️ for health-conscious foodies!
