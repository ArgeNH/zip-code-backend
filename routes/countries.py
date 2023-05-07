countries_dict = {
    (3, 3, 1): ["Canada"],
    (6, 0, 0): [
        "Colombia", "Belarus"
        "China", "Rusia", "Ecuador",
        "Paraguay", "India", "Kazakhstan",
        "Kirguistán", "Romania", "Nigeria",
        "Singapur", "Panama", "Tajikistan",
        "Trinidad y Tobago", "Turkmenistan",
        "Uzbekistan"
    ],
    (4, 0, 0): [
        "Australia", "Afganistan",
        "Albania", "Armenia",
        "Argentina", "Austria",
        "Bangladesh", "Belgica",
        "Bolivia", "Bulgaria",
        "Cabo Verde", "Isla de Navidad",
        "Isla Cocos", "Chipre", "China",
        "Lituania", "Holanda", "Portugal",
        "Luxemburgo", "South Africa", "Filipinas",
        "Nueva Zelanda", "Belgica", "Bangladesh",
        "Suiza", "Dinamarca", "Noruega", "Hungria",
        "Macedonia", "Eslovenia", "El Salvador",
        "Etiopia", "Tunez", "Haiti", "Paraguay",
        "Georgia", "Monzambique", "Libano",
        "Islas Maldivas", "Alemania", "Groenlandia",
        "Letonia", "Republica de Moldovia",
        "Liberia", "Liechtenstein", "Maldivas",
        "Moldova", "Venezuela", "Niger",
        "Norfolk Island", "Paraguay",
        "Svalbard & Jan Mayen Islands", "Zambia"
    ],
    (5, 0, 0): [
        "España", "Aland Islands",
        "Algeria", "Bhutan", "Cambodia",
        "Chad", "Costa Rica", "Croacia",
        "Francia", "Alegeria", "Korea del Sur",
        "Sri Lanka", "Mexico", "Malasya", "Pakistan",
        "Polonia", "Tailandia", " Replubica Dominicana",
        "Turkia", "Ucrania", "EEUU", "Israel", "Marruecos",
        "Senegal", "Vietnam", "Finlandia", "Cuba",
        "Egipto", "Estonia", "Alemania",
        "Guyana Francesa", "Macedonia", "Monaco",
        "Guadalope", "Guam", "Brazil",
        "Guatemala", "Honduras", "Italia",
        "Suecia", "Indonesia", "Iran", "Iraq",
        "Jordania", "Kenia", "Kosovo", "Mongolia",
        "Kuwait", "Serbia", "Laos", "Peru",
        "Libya", "Lithuania", "Taiwan", "Ciudad del Vaticano",
        "Maldivas", "Marshall Islands", "Micronesia",
        "Montenegro", "Myanmar", "Namibia", "Nepal",
        "Nueva Caledonia", "Nicaragua", "Grecia",
        "Northern Mariana Islands", "Palau",
        "Panama", "Puerto Rico", "Reunion",
        "Saint Barthélemy", "Saint Martin",
        "Saint Pierre and Miquelon", "San Marino"
        "Arabia Saudi", "Sudan", "Uruguay",
        "U.S. Virgin Islands", "Vatican",
        "Wallis and Futuna"
    ],
    (5, 0, 1): ["Grecia", "Republica Checa", "Eslovaquia"],
    (2, 4, 1): ["Reino Unido", "Gibraltar"],
    (3, 4, 1): ["Reino Unido"],
    (2, 1, 0): ["Irlanda"],
    (3, 2, 0): ["Andorra"],
    (4, 2, 0): [
        "Azerbaijan", "Islas Virgenes Britanicas",
        "Brunei"
    ],
    (4, 2, 1): ["Anguila", "Holanda"],
    (4, 4, 0): ["Argentina"],
    (4, 1, 0): ["Argentina"],
    (5, 2, 0): ["Barbados"],
    (2, 2, 1): ["Bermuda"],
    (0, 4, 1): ["Bermuda"],
    (8, 0, 1): ["Brazil"],
    (1, 5, 1): ["British Indian Ocean Territory"],
    (5, 2, 1): ["Islas Caiman"],
    (7, 0, 0): ["Chile"],
    (3, 0, 0): [
        "Islas Feroe", "India", "Mexico",
        "Islandia", "Korea del Sur", "Nigeria",
        "Madagascar", "Papua Nueva Guinea",
        "Ucrania", "Taiwan", "Japon", "Lesoto",
        "Bahrain", "Guinea", "Madagascar", "Oman",
        "Rusia", "Tajikistan", "Vatican"
    ],
    (2, 0, 0): [
        "Alemania", "Singapur",
        "Turkia"
    ],
    (2, 5, 0): ["Jamaica"],
    (7, 0, 1): [
        "Chile", "Japon", "Portugal"
    ],
    (1, 6, 1): [
        "Islas Mavinas", "Saint Helena", "Turks and Caicos Islands"
    ],
    (4, 3, 1): ["Malta", "Montserrat"],
    (3, 1, 0): ["Esuatini", "South Africa"]
}

patterns = {
    # Codigo postal de ESTADOS UNIDOS
    "ZIPCODE_US": [{"SHAPE": "dddd"}, {"ORTH": "-"}, {"SHAPE": "ddddd"}],
    # Codigo postal de CANADA
    "ZIPCODE_CA": [
        {"SHAPE": "XdX"},
        {"IS_SPACE": True, "OP": "?"},
        {"SHAPE": "dXd"},
    ],
    # Codigo postal de COLOMBIA, Belarus,
    "ZIPCODE_CO": [{"SHAPE": "dddddd"}],
    # Codigo postal de AUSTRALIA, AFGANISTAN,
    # Albania, Armenia, Argentina, Austria,
    #  Bangladesh, Belgica, Bulgaria, Cabo Verde
    # Codigo postal de ESPAÑA, Aland Islands, Algeria, Bhutan, Cambodia
    "ZIPCODE_ES": [{"SHAPE": "ddddd"}],
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
    "ZIPCODE_IRLANDA": [{"SHAPE": "Xdd"}],  # Codigo postal de IRLANDA
    "ZIPCODE_AD": [{"SHAPE": "XXddd"}],  # Codigo postal de ANDORRA
    # Codigo postal de Azerbaijan, Islas Virgenes Britanicas, Brunei
    "ZIPCODE_AZ": [{"SHAPE": "XXdddd"}],
    # Codigo postal de ANGUILA
    "ZIPCODE_AI": [{"SHAPE": "XX-dddd"}],
    # Codigo postal de Argentina
    "ZIPCODE_AR_ONE": [{"SHAPE": "XddddXXX"}],
    "ZIPCODE_AR_TWO": [{"SHAPE": "Xdddd"}],  # Codigo postal de Argentina
    "ZIPCODE_BB": [{"SHAPE": "XXddddd"}],  # Codigo postal de Barbados
    "ZIPCODE_BM_ONE": [
        {"SHAPE": "XX"},
        {"IS_SPACE": True, "OP": "?"},
        {"SHAPE": "dd"}
    ],  # Codigo postal de Bermuda
    "ZIPCODE_BM_TWO": [
        {"SHAPE": "XX"},
        {"IS_SPACE": True, "OP": "?"},
        {"SHAPE": "XX"}
    ],  # Codigo postal de Bermuda
    "ZIPCODE_BR": [{"SHAPE": "ddddd-ddd"}],  # Brazil
    "ZIPCODE_IO": [
        {"SHAPE": "XXdX"},
        {"IS_SPACE": True, "OP": "?"},
        {"SHAPE": "XX"}
    ],  # British Indian Ocean Territory
    "ZIPCODE_KY": [{"SHAPE": "XXd-dddd"}],  # Islas Caiman
    "ZIPCODE_AU": [{"SHAPE": "dddd"}],
        "ZIPCODE_CL": [{"SHAPE": "ddddddd"}],  # Chile
        "ZIPCODE_FK": [
            {"SHAPE": "XXXX"},
            {"IS_SPACE": True, "OP": "?"},
            {"SHAPE": "dXX"}
    ],  # Islas Malvinas
    "ZIPCODE_FO": [{"SHAPE": "ddd"}],  # Islas Feroe
    "ZIPCODE_GF": [{"SHAPE": "973dd"}],  # Guyana Francesa
        "ZIPCODE_GFP": [{"SHAPE": "987dd"}],  # Polinesia Frances
        "ZIPCODE_NC": [{"SHAPE": "988dd"}],  # Nueva Caledonia
        "ZIPCODE_GP": [{"SHAPE": "971dd"}],  # Guadalope
        "ZIPCODE_DE": [{"SHAPE": "dd"}],  # Alemania 1
        "ZIPCODE_JM": [{"SHAPE": "XXXXdd"}],  # Jamaica
        "ZIPCODE_JP": [{"SHAPE": "ddd-dddd"}],  # Japon
        "ZIPCODE_MT": [
            {"SHAPE": "XXX"},
            {"IS_SPACE": True, "OP": "?"},
            {"SHAPE": "dddd"}
    ],  # Malta
    "ZIPCODE_NL": [
            {"SHAPE": "dddd"},
            {"IS_SPACE": True, "OP": "?"},
            {"SHAPE": "XX"}
    ],  # Holanda
    "ZIPCODE_PT": [
            {"SHAPE": "dddd"},
            {"IS_SPACE": True, "OP": "?"},
            {"SHAPE": "ddd"}
    ],  # Holanda
    # Saint Vincent and the Grenadines
    "ZIPCODE_VC": [{"SHAPE": "XXdddd"}],
        "ZIPCODE_SZ": [{"SHAPE": "Xddd"}],
}
