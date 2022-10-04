from email.mime import image
from django.db import models
from django.conf import settings

# Create your models here.

class Project(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title_image = models.ImageField(blank=True)
    technology_tag = models.ManyToManyField('DevTechnology',blank=True )
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    
    


class DevTechnology(models.Model):
    name = models.CharField("기술 스택", max_length=30, unique=True)
    image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.name