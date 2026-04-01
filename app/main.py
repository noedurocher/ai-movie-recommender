from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.users_db import create_user
from app.auth import authenticate_user, create_access_token, get_current_user
from app.tmdb_client import get_popular_movies
from app.recommender import get_recommendations
from app.models import UserInput

app = FastAPI()
movies_cache = get_popular_movies()

# ---------------------------
# Signup Endpoint
# ---------------------------
@app.post("/signup")
def signup(username: str, password: str):
    if username in movies_cache:  # check if user exists
        raise HTTPException(status_code=400, detail="User already exists")
    create_user(username, password)
    return {"message": "User created successfully"}

# ---------------------------
# Login Endpoint
# ---------------------------
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

# ---------------------------
# Protected Recommend Endpoint
# ---------------------------
@app.post("/recommend")
def recommend(user_input: UserInput, current_user=Depends(get_current_user)):
    recommended = get_recommendations(user_input.favorite_movies, movies_cache)
    return {"recommended_movies": recommended, "user": current_user["username"]}

import os

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)