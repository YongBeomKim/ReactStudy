from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.


class Video(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField()
    photo = models.ImageField()
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("mytube:detail", args=[self.pk])


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="mov")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse("mytube:detail", args=[self.pk])
