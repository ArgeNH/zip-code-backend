from fastapi import APIRouter, Request, Response, status
from requests import get
from json import loads
from dotenv import dotenv_values
import uuid

# from models import location
from config import db
from codes import get_country_name

# Location = location.Location
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

    # Analisis estructural del codigo postal

    # Comprobar si esta en la db
    # Si esta, retornar el objeto
    # Si no esta, hacer la peticion a la API y guardar el objeto en la db

    try:
        location_array = dbZip.locations.find(
            {"postal_code": zipcode}, {"_id": 0})
        # print(list(location_array))

        if (len(list(location_array.clone())) > 0):
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

            zipcodes_array = data["results"][f"{zipcode}"]

            if isinstance(zipcodes_array, list):
                for zipcode in zipcodes_array:
                    country = get_country_name(zipcode["country_code"])
                    zipcode["country_code"] = country
                    zipcode["_id"] = str(uuid.uuid4())

                dbZip.locations.insert_many(zipcodes_array)

                return {"zipcode": zipcode}
            else:
                print("Error: el resultado de la API no es una lista.")

        return {"zipcode": list(location_array.clone())}
    except TypeError as e:
        print(e.args)
