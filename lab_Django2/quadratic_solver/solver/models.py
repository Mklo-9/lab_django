from django.db import models

class EquationSolution(models.Model):
    equation = models.CharField(max_length=100)
    root1 = models.FloatField(default=0.0)
    root2 = models.FloatField(default=0.0)
    correct = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Equation: {self.equation} - Correct status: {self.correct}"
