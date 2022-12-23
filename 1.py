DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'winter': {
        'картошка, шт': 1,
        'яйцо, шт': 1,
        'колбаса, г': 0.3,
        'огурец, шт': 1
    }
}
# for k, v in DATA.items():
#     if k == 'pasta':
#         print(v)
result = {}
amount_portion = 4
for k, v in DATA['omlet'].items():
    result[k] = v
    for key, value in result.items():
        print(value*amount_portion)
