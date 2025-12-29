from django.db import models

# Create your models here.

from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.FileField(upload_to='skills/')

    def __str__(self):
        return self.name

