from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

class Badge(models.Model):
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=100)
    max_progress = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to="badges/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO: functionality to check for the badges

    def __str__(self):
        return f"<Badge: {self.name}>"


class Perk(models.Model):

    class PerkStatus(models.TextChoices):
        ACTIVE = "AC", _("Active")
        INACTIVE = "IN", _("Inactive")

    name = models.CharField(max_length=100, help_text=_("A short catchy name for the perk"))
    short_description = models.CharField(max_length=255, help_text=_("A short description of the perk, what it offers"))
    long_description = models.TextField(help_text=_("Here you can go into detail about what the perk is about, why you are offering it, etc."), blank=True)
    image = models.ImageField(upload_to="perks")
    status = models.CharField(max_length=2, choices=PerkStatus.choices, default=PerkStatus.ACTIVE, null=False)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    required_badges = models.ManyToManyField(Badge, help_text=_("Badges that act as a eligibility criterion for this perk. Use Ctrl to select multiple badges."))
    # expiry = models.DateTimeField(default=after_100_years, help_text=_("Time until which the perk can be claimed. Default is 100 years"))
    quantity = models.IntegerField(default=100000, help_text=_("The number of times that this perk can be claimed, if it is only in limited quantity"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.long_description is None:
            self.long_description = ""

    def __str__(self):
        return f"<Perk: {self.name}"


class BadgeProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.RESTRICT)
    progress = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    unlocked = models.BooleanField(default=False)

    def clean(self):
        if self.progress >= self.badge.max_progress:
            self.unlocked = True

# def validate_expiry_greater_than_today(expiry):
#     if expiry < datetime.today():
#         raise ValidationError(_("%(end_date)s should be today or later than today. Perks will be active until 11:59PM IST on this date"))
# 
# 
# def after_100_years():
#     return datetime.now() + datetime.timedelta(year=100)
