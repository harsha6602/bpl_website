# Generated by Django 4.1.4 on 2023-01-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpl_app", "0004_playersinfo_sport"),
    ]

    operations = [
        migrations.AddField(
            model_name="criketscores",
            name="overs",
            field=models.IntegerField(default=0),
        ),
    ]
