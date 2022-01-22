from django.contrib.auth.models import AbstractUser
from django.db import models

from perks.models import Badge


class User(AbstractUser):
    # TODO: add profile photo, some other details

    badges = models.ManyToManyField("perks.Badge", through="perks.BadgeProgress")
    perks_won = models.ManyToManyField("perks.Perk", blank=False)

    avatar = models.ImageField(upload_to="avatars/")

    @property
    def unlocked_badges(self):
        return Badge.objects.filter(id__in=self.badgeprogress_set.filter(unlocked=True).values("badge_id")).all()

    @property
    def locked_badges(self):
        return Badge.objects.exclude(id__in=self.badgeprogress_set.filter(unlocked=True).values("badge_id"))
