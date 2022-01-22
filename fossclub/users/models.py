from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # TODO: add profile photo, some other details

    badges = models.ManyToManyField("perks.Badge", through="perks.BadgeProgress")
    perks_won = models.ManyToManyField("perks.Perk")

    @property
    def unlocked_badges(self):
        return self.badges.filter(unlocked=True)
