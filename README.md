# AI Movie Recommendation API

A FastAPI-based backend that provides movie recommendations using machine learning (TF-IDF + cosine similarity) and real-time data from TMDB API.

## Features

- JWT Authentication (Signup/Login)
- AI-based movie recommendations
- Integration with TMDB API
- RESTful API built with FastAPI

## Tech Stack

- Python
- FastAPI
- scikit-learn
- JWT Authentication
- TMDB API

## Run Locally

pip install -r requirements.txt
uvicorn app.main:app --reload

## API Endpoints

POST /signup  
POST /token  
POST /recommend (Protected)

## Example Request

{
"favorite_movies": ["Inception", "Jumanji"]
}
