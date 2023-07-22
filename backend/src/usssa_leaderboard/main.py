from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List


class AwardCategory(BaseModel):
    name: str
    value: float|int

class Contingent(BaseModel):
    contingent_name: str

class CategoryField(BaseModel):
    name: str
    options: List[str]

class Category(BaseModel):

    name: str
    fields: List[CategoryField]


class Leaderboard(BaseModel):
    name: str
    description: str | None
    award_category: List[AwardCategory]
    contingents: List[Contingent]
    categories: List[Category]

app = FastAPI()


@app.post("/leaderboard")
async def create_leaderboard(leaderboard:Leaderboard):
    return {"message": "Hello World"}
