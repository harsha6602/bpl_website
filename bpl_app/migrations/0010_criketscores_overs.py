# Generated by Django 4.1 on 2023-01-26 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpl_app", "0009_remove_criketscores_overs"),
    ]

    operations = [
        migrations.AddField(
            model_name="criketscores",
            name="overs",
            field=models.IntegerField(default=0),
        ),
    ]
