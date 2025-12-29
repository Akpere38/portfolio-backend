from django.db import models

# Create your models here.


from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image= models.FileField(upload_to='skills/', blank=True, null=True)
    demo_url = models.URLField(blank=True)
    code_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
