from django.shortcuts import render
from django.http import HttpResponse
import math

def solve_quadratic(request):
    a = float(request.GET.get('a', 0))
    b = float(request.GET.get('b', 0))
    c = float(request.GET.get('c', 0))

    equation = f"{a}x² + {b}x + {c} = 0"
    if a == 0 :
        if b == 0:
            if c == 0:
                roots = "Уравнение имеет бесконечно много решений."
            else:
                roots = "Уравнение не имеет решений."
        else:
            x = -c / b
            roots = f"Линейное уравнение: x = {x}"
    else:
        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            roots = f"Два корня: x₁ = {x1}, x₂ = {x2}"
        elif discriminant == 0:
            x = -b / (2*a)
            roots = f"Один корень: x = {x}"
        else:
            roots = "Нет действительных корней"

    context = {
        'equation': equation,
        'roots': roots,
    }
    return render(request, 'solver/solution.html', context)