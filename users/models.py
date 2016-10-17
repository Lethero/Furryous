from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

upload_location = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    date_of_birth = models.DateField(blank=True, null=True)
    date_created = models.DateField()
    bio = models.TextField(default="", blank=True)
    avatar = models.ImageField(storage=upload_location, null=True,
                               verbose_name="Profile Picture", blank=True)

    # Add something to track the user favorites.

    class Meta:
        ordering = ("-user",)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user, date_created=timezone.now())
        user_profile.save()

post_save.connect(create_profile, sender=User)