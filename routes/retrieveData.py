from pandas import read_excel
from codes import get_country_name
from config import db
import uuid

dbZip = db.dbZip

locations = []


def loadExcelData():
    df = read_excel(
        "/Users/xxxxx/Downloads/geonames-postal-code@public.xlsx")

    df = df.fillna("")

    for index, row in df.iterrows():
        location = {
            "_id": str(uuid.uuid4()),
            "country_code": row["country code"],
            "postal_code": row["postal code"],
            "latitude": row["latitude"],
            "longitude": row["longitude"],
            "city": row["place name"],
            "state": row["admin name1"],
            "province": row["admin code2"],
            "country_name": get_country_name(row["country code"]),
            "city_en": row["place name"],
            "state_en": row["admin name1"],
            "state_code": row["admin code1"],
            "province_code": row["admin code2"]
        }
        locations.append(location)

    dbZip.locations.insert_many(locations, ordered=False)
