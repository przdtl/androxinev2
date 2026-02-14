from pydantic import BaseModel


class ListCategoriesResponse(BaseModel):
    categories: list[str]
