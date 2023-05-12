import spacy
import re
from spacy.matcher import Matcher, PhraseMatcher
from .countries import countries_dict, patterns

nlp = spacy.load("en_core_web_sm")


def is_valid_postal_code(zipcode: str):

    matcher = Matcher(nlp.vocab)

    digit, letter, alpha = contar_caracteres(zipcode)

    for name, pattern in patterns.items():
        matcher.add(name, [pattern])

    doc = nlp(zipcode)

    matches = matcher(doc)

    country_possible = []
    for match_id, start, end in matches:
        codigo_postal = doc[start:end]
        match_name = nlp.vocab.strings[match_id]
        country_possible.append(match_name)

    if len(matches) == 0:
        return {
            "message": "El código postal no es válido",
            "valid": False,
            "countries": country_possible,
            "data": {
                "letters": letter,
                "digits": digit,
                "characters": alpha,
                "pattern": countries_dict.get((digit, letter, alpha), [])
            }
        }

    return {
        "message": "Código postal válido",
        "valid": True,
        "countries": country_possible,
        "data": {
            "letters": letter,
            "digits": digit,
            "characters": alpha,
            "pattern": countries_dict.get((digit, letter, alpha), [])
        }
    }


def verificar_codigo_postal(zipcode, data):
    matching_countries = []

    for entry in data:
        country = entry["Country"]
        regex = entry["Regex"]

        if re.match(regex, zipcode):
            matching_countries.append(country)

    return matching_countries


def contar_caracteres(texto):
    letters, digits, alpha = 0, 0, 0
    for caracter in texto:
        if caracter.isalpha():
            letters += 1
        elif caracter.isdigit():
            digits += 1
        else:
            alpha += 1
    return digits, letters, alpha
