# Generated by Django 4.0.1 on 2022-01-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perks', '0002_badge_max_progress_badgeprogress'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='badges',
            field=models.ManyToManyField(through='perks.BadgeProgress', to='perks.Badge'),
        ),
        migrations.AddField(
            model_name='user',
            name='perks_won',
            field=models.ManyToManyField(to='perks.Perk'),
        ),
    ]
