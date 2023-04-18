from fastapi import APIRouter
from requests import get
from json import loads

router = APIRouter(
    prefix="/zipcode",
    tags=["zipcode"],
)


@router.get("/{zipcode}")
async def read_zipcode(zipcode: str):

    headers = {
        "apikey": "API-KEY",
    }
    params = (
        ("codes", f"{zipcode}"),
    )

    response = get(
        'https://app.zipcodebase.com/api/v1/search', headers=headers, params=params)
    print(response.text)
    return {"zipcode": zipcode}
