import numpy as np

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

brand_chars = (  # dBrand
    (10, 4, .2918, .290),
    (4.5, .5, .2326, .52),
    (3, .5, .1613, .680),
    (7, 1.3, .0924, .77),
    (4, .2, .0552, .83),
    (3, 1.25, .053, .88),
    (5, .8, .0325, .915),
    (9, 1, .03, .945),
    (13, 2, .027, .975),
    (5, 1.5, .0242, 1)
)

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