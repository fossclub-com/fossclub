from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from allauth.socialaccount.models import SocialAccount

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


@receiver(post_save, sender=SocialAccount)
def update_badges(sender, instance, created=False, **kwargs):
    print("post save update_followers_badges")

    from perks.tasks import check_followers_badge, check_oauth_badge

    if created:
        user = instance.user
        check_followers_badge(user)
        check_oauth_badge(user)
