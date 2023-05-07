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

    # verificar_codigo_postal(zipcode, patterns)

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


def verificar_codigo_postal(texto, patterns):
    doc = nlp(texto)
    for pattern_name, pattern in patterns.items():
        for i, token in enumerate(doc):
            token_match = True
            for j, cond in enumerate(pattern):
                if i + j < len(doc):
                    token_to_check = doc[i + j]
                    if "SHAPE" in cond and token_to_check.shape_ != cond["SHAPE"]:
                        token_match = False
                        break
                    if "ORTH" in cond and token_to_check.text != cond["ORTH"]:
                        token_match = False
                        break
                    if "IS_SPACE" in cond and token_to_check.is_space != cond["IS_SPACE"]:
                        token_match = False
                        break
                else:
                    token_match = False
                    break

            if token_match:
                print(f"El texto coincide con el patrón: {pattern_name}")
                return True

        if not token_match:
            print(
                f"Fallo en la comprobación del patrón {pattern_name} en el token {i + j}: {doc[i + j].text} (condición: {cond})")

    print("No se encontró ningún patrón coincidente.")
    return False


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
