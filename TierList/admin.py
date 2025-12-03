from django.contrib import admin
from .models import Ranking, Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ["ranking", "image"]
    list_filter = ["ranking"]
    search_fields = ["ranking__list_name"]


class TierAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Ranking", {"fields": ["list_name"]}),
        ("Publish date", {"fields": ["creation_date"], "classes": ["collapse"]}),
        ("Items", {"fields": ["tier_config"], "classes": ["collapse"]}),
    ]

    list_display = ["list_name", "creation_date"]
    list_filter = ["list_name"]
    search_fields = ["list_name"]

admin.site.register(Ranking, TierAdmin)
admin.site.register(Image, ImageAdmin)

