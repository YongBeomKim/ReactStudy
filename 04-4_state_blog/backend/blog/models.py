from django.db import models

# Create your models here.
from datetime import datetime
from django.template.defaultfilters import slugify


class Categories(models.TextChoices):
    WORLD = "world"
    ENVIRONMENT = "environment"
    TECHNOLOGY = "technology"
    DESIGN = "design"
    CULTURE = "culture"
    BUSINESS = "business"
    POLITICS = "politics"
    OPINION = "opinion"
    SCIENCE = "science"
    HEALTH = "health"
    STYLE = "style"
    TRAVEL = "travel"


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.CharField(
        max_length=50,
        choices=Categories.choices,
        default=Categories.WORLD,
    )
    thumbnail = models.ImageField(upload_to="photos/%y/%m/%d/")
    excerpt = models.CharField(max_length=50)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()
