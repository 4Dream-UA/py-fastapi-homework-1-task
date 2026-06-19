from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class MovieDetailResponseSchema(BaseModel):
    """Full representation of a single movie, matching the MovieModel fields."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    date: str
    score: float
    genre: Optional[str] = None
    overview: Optional[str] = None
    crew: Optional[str] = None
    orig_title: Optional[str] = None
    status: Optional[str] = None
    orig_lang: Optional[str] = None
    budget: Optional[float] = None
    revenue: Optional[float] = None
    country: Optional[str] = None


class MovieListItemSchema(MovieDetailResponseSchema):
    """Movie representation used inside the paginated list response.

    Identical to the detail schema; kept as a separate name so the list
    item shape can diverge from the detail shape later without breaking
    callers.
    """
    pass


class MovieListResponseSchema(BaseModel):
    """Paginated list of movies."""

    movies: List[MovieListItemSchema]
    prev_page: Optional[str] = Field(default=None)
    next_page: Optional[str] = Field(default=None)
    total_pages: int
    total_items: int
