from django.db import models


# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    register = models.CharField(max_length=30, unique=True)
    birth_date = models.DateField()
    classroom = models.CharField(max_length=20)
    phone = models.CharField(unique=True, blank=True, max_length=10)
    city = models.CharField(max_length=20)
    gender = models.BooleanField()

    def __str__(self):
        return f"{self.last_name} - {self.first_name}"

    class Meta:
        verbose_name = "Eleve"
        verbose_name_plural = "Eleves"
