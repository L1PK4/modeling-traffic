import numpy as np

from src.car.car import Car

coatings = (
    "Асфальтное",
    "Бетонное",
    "Гравийное"
)
liftings = (
    "< 5.5 тонн",
    ">= 5.5 тонн"
)

allowed_speed = (
    (110 * 3.6, 90 * 3.6),
    (90 * 3.6, 70 * 3.6),
    (85 * 3.6, 60 * 3.6)
)

signs = (
    (
        (False, 50 * 3.6),
        (False, None),
        (False, 40 * 3.6),
        (False, None),
        (False, 60 * 3.6),
        (False, None),
    ),
    (
        (False, 50 * 3.6),
        (True, None),
        (False, 40 * 3.6),
        (True, None),
        (False, 60 * 3.6),
        (True, None),
    )
)

# road_lines = (
#     "Однополосная",
#     "Двухполосная"
# )

cars = [  # dBrand
    Car(0, "КАМАЗ", 10, 4, .2918, .290),
    Car(1, "ГАЗ", 4.5, .5, .2326, .52),
    Car(2, "ЗИЛ", 3, .5, .1613, .680),
    Car(3, "МАЗ", 7, 1.3, .0924, .77),
    Car(4, "Урал", 4, .2, .0552, .83),
    Car(5, "САЗ", 3, 1.25, .053, .88),
    Car(6, "Volvo", 5, .8, .0325, .915),
    Car(7, "MAN", 9, 1, .03, .945),
    Car(8, "Scania", 13, 2, .027, .975),
    Car(9, "Mercedes Benz", 5, 1.5, .0242, 1)
]

brands = (
    "КАМАЗ",
    "ГАЗ",
    "ЗИЛ",
    "МАЗ",
    "Урал",
    "САЗ",
    "Volvo",
    "MAN",
    "Scania",
    "Mercedes Benz",
)

S = 30 * 1000
Tk = 60 * 60 * 18
dt = 120
regimes = 6
N = 1000
lambda_ = .056
dTb = 3.6
dv = 20 * 3.6
