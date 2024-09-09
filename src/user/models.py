from django.db import models


# Create your models here.
class User(models.Model):
    pseudo = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=15)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pseudo

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
