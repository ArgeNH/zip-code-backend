from fastapi import APIRouter, Request, Path, UploadFile, File
from requests import get
from json import loads
from dotenv import dotenv_values
import uuid
import csv

from config import db
from codes import get_country_name

from .isValidZipcode import is_valid_postal_code, verificar_codigo_postal
from .countries import dataCountries

dbZip = db.dbZip

config = dotenv_values(".env")

router = APIRouter(
    prefix="/zipcode",
    tags=["zipcode"],
)


@router.get("/{zipcode}")
async def read_zipcode(zipcode: str = Path(..., min_length=1), request: Request = None):

    if len(zipcode) == 0:
        return {"error": "Debe ingresar un código postal"}

    # Analisis estructural del codigo postal

    code = is_valid_postal_code(zipcode)

    if code["valid"] == False:
        return {
            "message": "El código postal no es válido",
            "valid": False,
            "status": 404,
            zipcode: [],
            "code": code
        }

    sintantic = verificar_codigo_postal(zipcode, dataCountries)

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

            if data["results"] == []:
                return {
                    "message": "Código postal no encontrado",
                    "status": "404",
                    "valid": False,
                    "zipcode": [],
                    "code": code
                }

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
                    "status": 200,
                    "valid": True,
                    "zipcode": list(location_added),
                    "code": code
                }
            else:
                return {
                    "message": "Código postal no encontrado. No es una lista",
                    "status": "404",
                    "valid": False,
                    "zipcode": [],
                    "code": code
                }

        return {
            "message": "Código postal encontrado.",
            "status": 200,
            "valid": True,
            "zipcode": list(location_array),
            "code": code
        }
    except TypeError as e:
        return {
            "message": f"Error {e.args}",
            "status": 500,
            "valid": False,
            "zipcode": [],
            "code": code
        }
# brew services start mongodb-community@6.0


@router.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        rows = csv.reader(contents.decode().splitlines(), delimiter=',')

        codes = []
        for row in rows:
            codes.append(row)

        validate_codes = []

        for code in codes[0]:
            response = is_valid_postal_code(code)

            if response["valid"] == True:

                location_array = list(
                    dbZip.locations.find({"postal_code": code}))

                if (len(location_array) > 0):
                    print("Ya existe")
                else:
                    headers = {
                        "apikey": config["API_KEY"],
                    }
                    params = (
                        ("codes", f"{code}"),
                    )

                    responseApi = get(
                        'https://app.zipcodebase.com/api/v1/search', headers=headers, params=params)
                    data = responseApi.json()

                    if data["results"] == []:
                        return {
                            "message": "Código postal no encontrado",
                            "status": "404",
                            "valid": False,
                            "zipcode": [],
                            "code": code
                        }

                    zipcodes_array = data["results"][f"{code}"]

                    location_added = []

                    if isinstance(zipcodes_array, list):
                        for zip in zipcodes_array:
                            country = get_country_name(zip["country_code"])
                            zip["country_name"] = country
                            zip["_id"] = str(uuid.uuid4())
                            location_added.append(zip)

                        dbZip.locations.insert_many(zipcodes_array)

                        validate_codes.append({
                            "code": code,
                            "data": response,
                            "zipcodes": list(location_added),
                            "message": "Código postal válido",
                            "db": True
                        })

                    else:
                        return {
                            "message": "Código postal no encontrado. No es una lista",
                            "status": "404",
                            "valid": False,
                            "zipcode": [],
                            "code": code
                        }

                if len(list(filter(lambda x: x["code"] == code, validate_codes))) == 0:
                    validate_codes.append({
                        "code": code,
                        "data": response,
                        "zipcodes": list(location_array),
                        "message": "Código postal válido"
                    })
                else:
                    print("Ya exist en el array")

            else:
                validate_codes.append({
                    "code": code,
                    "data": response,
                    "message": "Código postal no válido"
                })

        return {
            "message": "Archivo leido con exito",
            "status": 200,
            "valid": True,
            "zipcode": validate_codes,
            "code": [],
            "filename": file.filename
        }
    except TypeError as e:
        return {
            "message": f"Error: {e.args}",
            "status": 500,
            "valid": False,
            "zipcode": [],
            "code": []
        }
    finally:
        file.file.close()
