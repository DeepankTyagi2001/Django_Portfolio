from django.db import models
from django.db.models import Model
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to="project_images/", blank=True)
    URL= models.URLField(max_length=200, default="https://github.com/DeepankTyagi2001?tab=repositories")
