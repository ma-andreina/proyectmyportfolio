from django.db import models
from django.db.models import CharField, URLField
from django.db.models import ImageField

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images')
    url = URLField(blank=True)
    languages = models.CharField(max_length=150, blank=True, help_text="Lenguajes utilizados en el proyecto, separados por coma.")

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"