from django.contrib import admin

from .models import Badge, BadgeProgress, Perk

admin.site.register(Badge)
admin.site.register(Perk)
admin.site.register(BadgeProgress)
