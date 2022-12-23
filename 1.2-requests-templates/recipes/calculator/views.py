from django.shortcuts import render
from django.http import HttpResponse


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

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def omlet(request):
    template_name = 'calculator/index.html'
    amount_portion = int(request.GET.get('servings', 1))
    result = {}
    for k, v in DATA['omlet'].items():
        result[k] = round(v * amount_portion, 1)
    context = {
        'recipe': result
    }
    return render(request, template_name, context)


def pasta(request):
    template_name = 'calculator/index.html'
    amount_portion = int(request.GET.get('servings', 1))
    result = {}
    for k, v in DATA['pasta'].items():
        result[k] = round(v * amount_portion, 1)
    context = {
        'recipe': result
    }
    return render(request, template_name, context)


def buter(request):
    template_name = 'calculator/index.html'
    amount_portion = int(request.GET.get('servings', 1))
    result = {}
    for k, v in DATA['buter'].items():
        result[k] = round(v * amount_portion, 1)
    context = {
        'recipe': result
    }
    return render(request, template_name, context)

def winter(request):
    template_name = 'calculator/index.html'
    amount_portion = int(request.GET.get('servings', 1))
    result = {}
    for k, v in DATA['winter'].items():
        result[k] = round(v * amount_portion, 1)
    context = {
        'recipe': result
    }
    return render(request, template_name, context)
