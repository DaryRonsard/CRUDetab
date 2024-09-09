from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    subject_taught = models.CharField(max_length=20)
    next_class = models.CharField(max_length=50, null=True, blank=True)
    next_meeting_topic = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(unique=True, blank=True, max_length=10)
    city = models.CharField(max_length=20)
    gender = models.BooleanField()
    vacant = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.birth_date} - {self.subject_taught}"

    class Meta:
        verbose_name = "Profeseur"
        verbose_name_plural = "Professeurs"
