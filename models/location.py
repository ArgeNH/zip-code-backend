from pydantic import BaseModel, Field


class Location(BaseModel):
    id: str = Field(..., alias="_id")
    city: str = Field(...)
    state: str = Field(...)
    country: str = Field(...)
    postal: str = Field(...)
    latitude: str = Field(...)
    longitude: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "5f4e7d4b0a4e7b8e1b1c9a9d",
                "city": "San Francisco",
                "state": "California",
                "country": "United States",
                "postal": "94102",
                "latitude": "37.781",
                "longitude": "-122.411"
            }
        }
