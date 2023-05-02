from fastapi import APIRouter, Request, Response, status, Path
from requests import get
from json import loads
from dotenv import dotenv_values
import uuid

# from models import location
from config import db
from codes import get_country_name

# import fuction is_valid_postal_code from isValidZipcode.py
from .isValidZipcode import is_valid_postal_code

# Location = location.Location
dbZip = db.dbZip

config = dotenv_values(".env")

router = APIRouter(
    prefix="/zipcode",
    tags=["zipcode"],
)


@router.get("/{zipcode}")
async def read_zipcode(zipcode: str = Path(..., min_length=1), request: Request = None):

    """ if len(request.path_params["zipcode"]) == 0:
        return {"error": "Debe ingresar un código postal"} """

    if len(zipcode) == 0:
        return {"error": "Debe ingresar un código postal"}

    # Analisis estructural del codigo postal

    code = is_valid_postal_code(zipcode)

    print(code)

    # Comprobar si esta en la db
    # Si esta, retornar el objeto
    # Si no esta, hacer la peticion a la API y guardar el objeto en la db

    # spaCy

    try:
        location_array = list(dbZip.locations.find({"postal_code": zipcode}))

        if (len(location_array) > 0):
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

            location_added = []

            if isinstance(zipcodes_array, list):
                for zip in zipcodes_array:
                    country = get_country_name(zip["country_code"])
                    zip["country_name"] = country
                    zip["_id"] = str(uuid.uuid4())
                    location_added.append(zip)

                dbZip.locations.insert_many(zipcodes_array)

                return {
                    "message": "Código postal encontrado.",
                    "status": "200",
                    "zipcode": list(location_added)
                }
            else:
                print("Error: el resultado de la API no es una lista.")

        return {
            "message": "Código postal encontrado.",
            "status": "200",
            "zipcode": location_array
        }
    except TypeError as e:
        print(e.args)
