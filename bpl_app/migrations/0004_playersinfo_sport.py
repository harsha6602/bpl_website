# Generated by Django 4.1 on 2023-01-21 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpl_app", "0003_teamsinfo_sport"),
    ]

    operations = [
        migrations.AddField(
            model_name="playersinfo",
            name="sport",
            field=models.CharField(default="null", max_length=12),
        ),
    ]
