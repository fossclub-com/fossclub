# Generated by Django 4.0.1 on 2022-01-22 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perks', '0003_badge_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='unit',
            field=models.CharField(default='followers', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perk',
            name='required_badges',
            field=models.ManyToManyField(help_text='Badges that act as a eligibility criterion for this perk. Use Ctrl to select multiple badges.', to='perks.Badge'),
        ),
    ]