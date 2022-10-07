from django.db import models
from django.conf import settings
from django.urls import reverse
import re

# Create your models here.

class Project(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title_image = models.ImageField(blank=True, upload_to="search_project/project/%Y/%m/%d")
    technology_tag = models.ManyToManyField('DevTechnology',blank=True )
    title = models.CharField(max_length=100)
    custom_tag = models.CharField(max_length=300)
    custom_tag_set = models.ManyToManyField('CustomTag',blank=True)
    content = models.TextField(max_length=500)
    location = models.CharField(max_length=100)

    @property
    def name(self):
        return f"{self.author.first_name} {self.author.last_name}"


    def __str__(self):
        return self.title
    
    def tag_parser(self):
        tag_name_list = re.findall(r"#([A-Za-z\dㄱ-힣]+)",self.custom_tag)
        tag_list = list()
        for tag_name in tag_name_list:
            tag, _ = CustomTag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)
        return tag_list

    def get_absolute_url(self):
        return reverse("projects:project_detail", kwargs={"pk": self.pk})
        #return reverse("projects:project_detail", args=[self.pk])


class DevTechnology(models.Model):
    name = models.CharField("기술 스택", max_length=30, unique=True)
    image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.name

class CustomTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
