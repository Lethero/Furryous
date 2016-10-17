from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

upload_location = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=256)
    alt = models.CharField(max_length=256, default="")
    date_posted = models.DateField(blank=True)
    mature = models.BooleanField(default=False)
    author = models.ForeignKey(User)
    # slug = models.SlugField()
    description = models.TextField(default="", blank=True)
    image = models.ImageField(storage=upload_location)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-date_posted",)