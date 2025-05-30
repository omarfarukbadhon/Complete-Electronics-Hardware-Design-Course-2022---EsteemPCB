designFile = "D:/Documents/DOCS/Batch-2/Mixed Signal Board Project - final/PDNAnalyzer_Output/Mixed Signal Board Project/odb.tgz"

powerNets = ["+12V", "NetC84_2", "+3V3"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J11", "1") ],
"ground_pins": [ ("J11", "3") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("Q1", "15"), ("Q1", "11"), ("Q1", "2") ],
"ground_pins": [ ("R19", "1") ],
"current": 3,
"Rpin": 0.05,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("Q2", "15"), ("Q2", "11"), ("Q2", "2") ],
"ground_pins": [ ("R43", "1") ],
"current": 3,
"Rpin": 0.05,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("U5", "13") ],
"ground_pins": [ ("U5", "1"), ("U5", "2"), ("U5", "4"), ("U5", "5") ],
"current": 0.01,
"Rpin": 16,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("U1", "1"), ("U1", "9"), ("U1", "24"), ("U1", "36"), ("U1", "48") ],
"ground_pins": [ ("U1", "8"), ("U1", "23"), ("U1", "35"), ("U1", "47") ],
"current": 0.15,
"Rpin": 2.96296296296296,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("U10", "3") ],
"ground_pins": [ ("U10", "1") ],
"current": 0.0001,
"Rpin": 1000,
}
]


voltage_regulators = [
{
"id": "6",
"type": "linear",

"in": [ ("U10", "3") ],
"out": [ ("U10", "4"), ("U10", "2") ],
"ref": [ ("U10", "1") ],

"v2": -8.2301,
"i1": 0,
"Ro": 0,
"Rpin": 0,
}
,
{
"id": "7",
"type": "linear",

"in": [ ("D5", "A") ],
"out": [ ("D5", "K") ],
"ref": [],

"v2": -0.443,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.1, 'Thickness': 0.0001},
        {'name': 'GND', 'Conductivity': 47000000, 'Thickness': 1.75E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.1, 'Thickness': 0.00126},
        {'name': 'VCC', 'Conductivity': 47000000, 'Thickness': 1.75E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.8, 'Thickness': 0.0001},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
