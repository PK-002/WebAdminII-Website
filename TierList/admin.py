from django.contrib import admin
from .models import Ranking, Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ["item_name", "tier_level", "position", "Ranking"]
    list_filter = ["tier_level", "Ranking"]
    search_fields = ["item_name", "tier_level"]


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

