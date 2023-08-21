from datetime import timedelta
from bson import ObjectId
from fastapi import Depends, FastAPI, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from slugify import slugify
from typing import Annotated, Dict, List, Optional
from usssa_leaderboard.config import settings

from . import auth
from .db import db, PyObjectId
from .schema import (
    CategoryResult,
    Contingent,
    ContingentBatch,
    Leaderboard,
    LeaderboardList,
    Ranking,
    UpdateLeaderboard
)

import pydantic
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str


app = FastAPI()





origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost:8081",
    "http://127.0.0.1:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await db.leaderboards.create_index("slug", unique=True)
    #await db.users.create_index("username")
    #await db.category_results.create_index("slug", unique=True)


@app.post("/token", response_model=auth.Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = await auth.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}



async def find_leaderboards():

    collection = db["leaderboards"]
    leaderboards = []
    async for leaderboard in collection.find():
        leaderboards.append(leaderboards)
        


@app.get(
    "/leaderboards",
    response_model=LeaderboardList,
    status_code=status.HTTP_200_OK
)
async def get_leaderboards() -> LeaderboardList:
    collection = db["leaderboards"]
    leaderboards = []
    for leaderboard in await collection.find().to_list(length=100):
        leaderboards.append(leaderboard)
        
    return LeaderboardList(leaderboards=leaderboards)



@app.post(
    "/leaderboards",
    response_model=Leaderboard,
    status_code=status.HTTP_201_CREATED)
async def create_leaderboard(
    token: Annotated[str, Depends(auth.get_current_active_user)],
    leaderboard:UpdateLeaderboard=Body(...)
):
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
    status_code=status.HTTP_200_OK
)
async def get_leaderboard(slug: str) -> Leaderboard:
    leaderboard_obj = await db["leaderboards"].find_one({"slug": slug})
    leaderboard= Leaderboard.parse_obj(leaderboard_obj)
    return leaderboard

@app.post(
    "/leaderboards/{slug}/category_results",
    response_model=Leaderboard,
    status_code=status.HTTP_201_CREATED
)
async def create_category_results(
    token: Annotated[str, Depends(auth.get_current_active_user)],
    slug: str, 
    category_result: CategoryResult
):
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

    return leaderboard



@app.post("/leaderboards/{slug}/contingents")
async def create_contingent(
    token: Annotated[str, Depends(auth.get_current_active_user)],
    slug: str,
    contingent:Contingent
):
    return {"message": "success"}

@app.post(
    "/leaderboards/{slug}/contingents/batch",
    response_model=Leaderboard,
    status_code=status.HTTP_201_CREATED
)
async def create_contingent_batch(
    token: Annotated[str, Depends(auth.get_current_active_user)],
    slug: str,
    batch:ContingentBatch
):
    leaderboard = await db.leaderboards.find_one({"slug": slug})
    print(leaderboard)
    leaderboard = Leaderboard.parse_obj(leaderboard)
    print(leaderboard)

    batch_values = []
    for contingent in batch.contingents:
        if leaderboard.is_existing_contingent(contingent):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"message": f"Contingent {contingent.name} already exists in leaderboard {slug}"}
            )
        else:
            batch_values.append(contingent.dict())

    original_leaderboard = await db.leaderboards.find_one_and_update(
        {"slug": slug},
        {"$push": {"contingents": {"$each": batch_values }}}
    )
    if not original_leaderboard:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"message": f"Unable to update"}
        )

    # update rankings
    updated_leaderboard = await db.leaderboards.find_one({"slug": slug})
    updated_leaderboard = Leaderboard.parse_obj(updated_leaderboard)
    return updated_leaderboard



#@app.patch("/leaderboard/{slug}/rankings")
#async def update_rankings(slug: str, leaderboard_rankings: LeaderboardRankings):

