from django.db import models

# Create your models here.
class Feed(models.Model):
    url = models.URLField(max_length=255, unique=True)
    def __repr__(self):
        return "<Feed 주소 '{}'>".format(self.url)