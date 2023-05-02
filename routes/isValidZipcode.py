import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")


def is_valid_postal_code(zipcode: str):

    matcher = Matcher(nlp.vocab)

    patterns = {
        # Codigo postal de ESTADOS UNIDOS
        "ZIPCODE_US": [{"SHAPE": "dddd"}, {"ORTH": "-"}, {"SHAPE": "ddddd"}],
        # Codigo postal de CANADA
        "ZIPCODE_CA": [
            {"SHAPE": "XdX"},
            {"IS_SPACE": True, "OP": "?"},
            {"SHAPE": "dXd"},
        ],
        "ZIPCODE_AU": [{"SHAPE": "dddd"}],  # Codigo postal de AUSTRALIA
        "ZIPCODE_CO": [{"SHAPE": "dddddd"}],  # Codigo postal de COLOMBIA
        "ZIPCODE_ES": [{"SHAPE": "ddddd"}],  # Codigo postal de ESPAÑA
        "ZIPCODE_GR": [
            {"SHAPE": "ddd"},
            {"IS_SPACE": True, "OP": "?"},
            {"SHAPE": "dd"}
        ],  # Codigo postal de GRECIA
        "ZIPCODE_UK_ONE": [
            {"SHAPE": "XXd"},
            {"IS_SPACE": True, "OP": "?"},
            {"SHAPE": "dXX"}
        ],
        "ZIPCODE_UK_TWO": [
            {"SHAPE": "XXdd"},
            {"IS_SPACE": True, "OP": "?"},
            {"SHAPE": "dXX"}
        ],
        "ZIPCODE_IRLANDA": [
            {"SHAPE": "Xdd"},
        ],
    }

    for name, pattern in patterns.items():
        matcher.add(name, [pattern])

    doc = nlp(zipcode)

    # verificar_codigo_postal(zipcode, patterns)

    matches = matcher(doc)

    for match_id, start, end in matches:
        codigo_postal = doc[start:end]
        match_name = nlp.vocab.strings[match_id]
        print(f"{match_name}: {codigo_postal.text}")

    print(matches)

    if len(matches) == 0:
        return {"message": "El código postal no es válido", "valid": False}

    return {"message": "Código postal válido", "valid": True}


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
