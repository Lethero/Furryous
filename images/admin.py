from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "date_posted", "author", "mature"]
    list_filter = ["date_posted", "author", "mature"]
    search_fields = ["title", "date_posted", "author"]
    date_hierarchy = "date_posted"
    prepopulated_fields = {
        "alt": ("title",)
    }
    save_on_top = True

    actions = ["mark_mature", "remove_mature"]

    def mark_mature(self, request, queryset):
        queryset.update(mature=True)

    def remove_mature(self, request, queryset):
        queryset.update(mature=False)

    mark_mature.short_description = "Mark mature"
    remove_mature.short_description = "Remove mature"