from fastapi import APIRouter, Request, Response, status
from requests import get
from json import loads
from dotenv import dotenv_values

from models import location
from config import db
from codes import get_country_name

Location = location.Location
dbZip = db.dbZip

config = dotenv_values(".env")

router = APIRouter(
    prefix="/zipcode",
    tags=["zipcode"],
)


@router.get("/{zipcode}")
async def read_zipcode(zipcode: str, request: Request):

    if len(zipcode) == 0:
        return {"error": "Debe ingresar un código postal"}

    # Comprobar si esta en la db
    # Si esta, retornar el objeto
    # Si no esta, hacer la peticion a la API y guardar el objeto en la db
    try:
        location = dbZip.locations.find_one({"postal": zipcode})

        if (location != None):
            print("Ya existe")
        else:
            headers = {
                "apikey": config["API_KEY"],
            }
            params = (
                ("codes", f"{zipcode}"),
            )

            response = get(
                'https://app.zipcodebase.com/api/v1/search', headers=headers, params=params)
            data = response.json()

            # print(data["results"][f"{zipcode}"][0])

            """ if (len(data["results"]) == 0):
                return {"error": "No se encontró el código postal"} """

            # print(data["results"][0]["country_code"])
            country = get_country_name(
                data["results"][f"{zipcode}"][0]["country_code"])
            print(country)
            """ if(data["status"] == "success"):
                dbZip.zipcodes.insert_one(data["data"][0])
            else:
                return {"error": "No se encontró el código postal"} """
            return {"zipcode": zipcode}
    except Exception as e:
        print(e)
