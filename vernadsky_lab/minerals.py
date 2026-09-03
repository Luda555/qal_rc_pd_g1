# vernadsky_lab/minerals.py

MINERAL_CATALOG = {
    "Тальк": {
        "formula": "Mg3Si4O10(OH)2",
        "hardness": 1,
        "origin": "Мадленберг, Австрія",
        "discovered": 1805
    },
    "Гіпс": {
        "formula": "CaSO4·2H2O",
        "hardness": 2,
        "origin": "Паризький басейн, Франція",
        "discovered": 1788
    },
    "Кальцит": {
        "formula": "CaCO3",
        "hardness": 3,
        "origin": "Фонтенбло, Франція",
        "discovered": 1836
    },
    "Флюорит": {
        "formula": "CaF2",
        "hardness": 4,
        "origin": "Камбрія, Велика Британія",
        "discovered": 1797
    },
    "Апатит": {
        "formula": "Ca5(PO4)3(F,Cl,OH)",
        "hardness": 5,
        "origin": "Саксонія, Німеччина",
        "discovered": 1786
    },
    "Ортоклаз": {
        "formula": "KAlSi3O8",
        "hardness": 6,
        "origin": "Карлові Вари, Чехія",
        "discovered": 1823
    },
    "Кварц": {
        "formula": "SiO2",
        "hardness": 7,
        "origin": "Житомирська область, Україна",
        "discovered": 1546
    },
    "Топаз": {
        "formula": "Al2SiO4(F,OH)2",
        "hardness": 8,
        "origin": "Острів Топазіос, Червоне море",
        "discovered": 1737
    },
    "Корунд": {
        "formula": "Al2O3",
        "hardness": 9,
        "origin": "Ратнапура, Шрі-Ланка",
        "discovered": 1798
    },
    "Алмаз": {
        "formula": "C",
        "hardness": 10,
        "origin": "Голконда, Індія",
        "discovered": 1556
    }
}

def get_mineral(name):
    if name in MINERAL_CATALOG:
        return MINERAL_CATALOG [name]
    return None

def register_mineral(name, formula, hardness, origin, discovered):
    if name in MINERAL_CATALOG:
        return (f"Мінерал {name} вже зареєстровано в каталозі")
    elif hardness > 10 or hardness < 1:
        return ("Некоректна твердість: має бути від 1 до 10")
    else:
        MINERAL_CATALOG[name] = {
            "formula": formula,
            "hardness": hardness,
            "origin": origin,
            "discovered": discovered
        }
        return MINERAL_CATALOG
