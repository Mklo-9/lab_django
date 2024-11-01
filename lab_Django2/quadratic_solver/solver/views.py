from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
from .models import EquationSolution

def generate_random_equation(request):
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)

    delta = b**2 - 4*a*c
    if delta > 0:
        root1 = round((-b + delta ** 0.5) / (2 * a), 2)
        root2 = round((-b - delta ** 0.5) / (2 * a), 2)
        roots = [root1, root2]
    elif delta == 0:
        root = round(-b / (2 * a), 2)
        roots = [root]
    else:
        roots = None

    request.session['generated_equation'] = {'a': a, 'b': b, 'c': c, 'roots': roots}

    return render(request, 'solver/trainer.html', {'a': a, 'b': b, 'c': c})

def trainer_check(request):
    equation_data = request.session.get('generated_equation')
    roots = equation_data.get('roots')

    user_root1 = float(request.GET.get('user_root1', 0))
    user_root2 = float(request.GET.get('user_root2', 0))
    user_roots = sorted([user_root1, user_root2])

    correct = False
    if roots is not None:
        correct = user_roots == sorted(roots)
        es = EquationSolution(
            equation = equation_data,
            root1 = user_root1,
            root2 = user_root2,
            correct = correct
            )
        es.save()

    return JsonResponse({
        'correct': correct,
        'user_roots': user_roots,
        'actual_roots': roots
    })

def solve_equation(request):
    try:
        a = float(request.GET.get('a', 0))
        b = float(request.GET.get('b', 0))
        c = float(request.GET.get('c', 0))
    except ValueError:
        return HttpResponse("Некорректные коэффициенты. Введите числа.")

    equation = f"{a}x² + {b}x + {c} = 0"
    delta = b**2 - 4*a*c

    roots = None
    if delta > 0:
        root1 = round((-b + delta ** 0.5) / (2 * a), 2)
        root2 = round((-b - delta ** 0.5) / (2 * a), 2)
        roots = [root1, root2]
    elif delta == 0:
        root = round(-b / (2 * a), 2)
        roots = [root]

    return render(request, 'solver/solve.html', {'equation': equation, 'roots': roots})