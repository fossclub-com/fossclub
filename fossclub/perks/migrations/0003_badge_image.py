# Generated by Django 4.0.1 on 2022-01-22 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perks', '0002_badge_max_progress_badgeprogress'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='image',
            field=models.ImageField(default='https://cdn.discordapp.com/attachments/910917612731498556/934399648146260018/badge.png', upload_to='badges/'),
            preserve_default=False,
        ),
    ]
