# Generated by Django 4.1 on 2023-01-21 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpl_app", "0002_playersinfo_player_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="teamsinfo",
            name="sport",
            field=models.CharField(default="null", max_length=12),
        ),
    ]
