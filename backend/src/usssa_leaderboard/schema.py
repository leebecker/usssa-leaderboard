from bson import ObjectId

from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel, ConfigDict, Field, validator
from pydantic_computed import Computed, computed
from typing import Dict, List, Optional, Union

from slugify import slugify
from usssa_leaderboard.db import db, PyObjectId

import nanoid

import pydantic
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str


class AwardValues(BaseModel):
    gold: Union[float, int]
    silver: Union[float, int]
    bronze: Union[float, int]
    descending: bool = True  # descending = True mean high scores come first


class AwardCategoryCount(BaseModel):
    name: str
    value: int

class Award(BaseModel):
    name: str
    contingent_id: str



class CategoryField(BaseModel):
    name: str
    options: List[str]

    @validator('options')
    def options_are_unique(cls, options):
        if len(set(options)) != len(options):
            raise ValueError("Duplicate options detected")
        return options


class CategoryDefinition(BaseModel):

    name: str
    fields: List[CategoryField]

    @validator('fields')
    def field_names_are_unique(cls, fields):
        if len(set([f.name for f in fields])) != len(fields):
            raise ValueError("Duplicate field names detected")
        return fields


class Category(BaseModel):
    name: str
    fields: List[str]

    def flattened(self):
        return '.'.join([self.name, *self.fields])

class CategoryResult(BaseModel):
    category: Category
    gold_contingent_id: List[str]       # these are arrays to allow
    silver_contingent_id: List[str]     # for multiple winners
    bronze_contingent_id: List[str]     # especially in bronze

class Contingent(BaseModel):

    id: Optional[str] = Field(default_factory=lambda: nanoid.generate(size=8))
    name: str
    country: str # fixme - this needs to generalize into a more flexible rendering for state, city, logo, etc
    is_national_federation: bool

class ContingentBatch(BaseModel):
    contingents: List[Contingent]


class Ranking(BaseModel):
    rank: int = 0
    contingent_id: str
    points: Union[int, float] = 0
    gold: int = 0
    silver: int = 0
    bronze: int = 0
    medals: int = 0

class UpdateRanking(BaseModel):
    contingent: Contingent
    award_category_counts: List[AwardCategoryCount]


class Leaderboard(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    slug: str
    description: Optional[str] = ""
    award_values: AwardValues
    categories: Optional[List[CategoryDefinition]] = Field(default_factory=list)
    contingents: Optional[List[Contingent]] = Field(default_factory=list)
    category_results: List[CategoryResult] = Field(default_factory=list)

    # rankings: Optional[List[Ranking]] = Field(default_factory=list)
    @computed('rankings')
    def compute_rankings(
        contingents: List[Contingent],
        category_results: List[CategoryResult],
        award_values: AwardValues,
        **kwargs
    ) -> List[Ranking]:

        totals = {c.id: Ranking(contingent_id=c.id) for c in contingents}

        for result in category_results:
            for contingent_id in result.gold_contingent_id:
                totals[contingent_id].gold += 1
                totals[contingent_id].medals += 1
                totals[contingent_id].points += award_values.gold

            for contingent_id in result.silver_contingent_id:
                totals[contingent_id].silver += 1
                totals[contingent_id].medals += 1
                totals[contingent_id].points += award_values.silver

            for contingent_id in result.bronze_contingent_id:
                totals[contingent_id].bronze += 1
                totals[contingent_id].medals += 1
                totals[contingent_id].points += award_values.silver


        rankings = sorted(
            totals.values(), 
            key=lambda row: (row.points, row.gold, row.silver, row.bronze),
            reverse=award_values.descending
        )

        rank_idx = 0
        last_points = None
        for r in rankings:
            if last_points is None or r.points < last_points:
                rank_idx += 1
                last_points = r.points
            r.rank = rank_idx

        return rankings


    def get_contingent(self, cid):
        return next(c for c in self.contingents if c.id == cid)

    def is_existing_category_result(self, result: CategoryResult):
        new_result_key = result.category.flattened()
        return new_result_key in (r.category.flattened() for r in self.category_results)

    def is_existing_contingent(self, contingent: Contingent):
        res = contingent.name in (c.name for c in self.contingents)
        return res




    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class LeaderboardList(BaseModel):
    leaderboards: List[Leaderboard]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UpdateLeaderboard(BaseModel):
    name: str
    description: Optional[str] = ""
    #awards: List[AwardDefinition]
    award_values: AwardValues
    categories: List[CategoryDefinition]
    contingents: List[Contingent]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class LeaderboardRankings(BaseModel):
    rankings: List[Ranking]



tmp= {
    "category": {"name": "Seni", "fields": ["Tunggal", "Male"]},
    "awards": [
        {"name": "Gold", "contingent_id": "yPc-SYDy"},
        {"name": "Silver", "contingent_id": "yPc-SYDy"},
        {"name": "Bronze", "contingent_id": "EBNQXchy"}
    ]
}
