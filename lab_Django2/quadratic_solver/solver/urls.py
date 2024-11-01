from django.urls import path
from . import views

urlpatterns = [
    path('solve/', views.solve_equation, name='solve_equation'),
    path('trainer/', views.generate_random_equation, name='trainer'),
    path('trainer/check/', views.trainer_check, name='trainer_check'),
]
