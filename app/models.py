from pydantic import BaseModel
from typing import List

# Request model for /recommend
class UserInput(BaseModel):
    favorite_movies: List[str]

# Response model for /recommend
class Recommendation(BaseModel):
    recommended_movies: List[str]
    user: str