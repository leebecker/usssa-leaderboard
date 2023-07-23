from bson import ObjectId
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel, ConfigDict, Field
from slugify import slugify
from typing import Dict, List, Optional
#from usssa_leaderboard.config import settings

from .db import db, PyObjectId
from .schema import (
    CategoryResult,
    Contingent,
    ContingentBatch,
    Leaderboard,
    Ranking,
    UpdateLeaderboard
)


app = FastAPI()

@app.on_event("startup")
async def startup():
    await db.leaderboards.create_index("slug", unique=True)
    await db.category_results.create_index("slug", unique=True)


@app.post("/leaderboards")
async def create_leaderboard(leaderboard:UpdateLeaderboard=Body(...)):
    leaderboard = jsonable_encoder(leaderboard)
    # compute and add slug
    leaderboard['slug'] = slugify(leaderboard['name'])
    new_leaderboard = await db["leaderboards"].insert_one(leaderboard)
    created_leaderboard = await db["leaderboards"].find_one({"_id": new_leaderboard.inserted_id})

    # fixup ID manually
    created_leaderboard['id'] = str(created_leaderboard['_id'])
    del[created_leaderboard['_id']]
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_leaderboard)


@app.get(
    "/leaderboards/{slug}",
    response_model=Leaderboard,
    status_code=status.HTTP_200_OK)
async def get_leaderboard(slug: str) -> Leaderboard:
    leaderboard = await db["leaderboards"].find_one({"slug": slug})

    return leaderboard

@app.post(
    "/leaderboards/{slug}/category_results",
    response_model=Leaderboard,
    status_code=status.HTTP_201_CREATED
)
async def create_category_results(slug, category_result: CategoryResult):
    leaderboard = await db.leaderboards.find_one({"slug": slug})
    leaderboard = Leaderboard.parse_obj(leaderboard)
    if leaderboard.is_existing_category_result(category_result):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": f"Result already exists for category {category_result.category.flattened()}"}
        )

    original_leaderboard = await db.leaderboards.find_one_and_update(
        {"slug": slug},
        {"$push": {"category_results": category_result.dict()}}
    )

    updated_leaderboard = await db.leaderboards.find_one({"slug": slug})

    leaderboard = Leaderboard.parse_obj(updated_leaderboard)
    rankings = [Ranking.dict(r) for r in leaderboard.compute_rankings()]

    updated_leaderboard = await db.leaderboards.find_one_and_update(
        {"slug": slug},
        {"$set": {"rankings": rankings}}
    )
    updated_leaderboard = await db.leaderboards.find_one({"slug": slug})
    return updated_leaderboard



@app.post("/leaderboards/{slug}/contingents")
async def create_contingent(slug, contingent:Contingent):
    return {"message": "success"}

@app.post("/leaderboard/{slug}/contingents/batch")
async def create_contingent_batch(slug, batch:ContingentBatch):
    return {"message": "success"}


#@app.patch("/leaderboard/{slug}/rankings")
#async def update_rankings(slug: str, leaderboard_rankings: LeaderboardRankings):

