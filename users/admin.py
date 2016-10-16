from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "date_created"]
    list_filter = ["date_created"]
    search_fields = ["user"]
    date_hierarchy = "date_created"