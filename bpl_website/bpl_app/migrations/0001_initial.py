# Generated by Django 4.1 on 2023-01-16 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TeamsInfo",
            fields=[
                (
                    "team_id",
                    models.CharField(
                        max_length=128, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("team_name", models.CharField(max_length=128, unique=True)),
                ("branch", models.CharField(max_length=128)),
                ("captain_phoneno", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="Umpires",
            fields=[
                (
                    "umpire_id",
                    models.CharField(
                        max_length=12, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("umpire_name", models.CharField(max_length=128)),
                ("phone_no", models.CharField(max_length=12, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="PlayersInfo",
            fields=[
                (
                    "player_id",
                    models.CharField(
                        max_length=12, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("player_role", models.CharField(max_length=128)),
                ("phone_no", models.CharField(max_length=12, unique=True)),
                ("branch", models.CharField(max_length=128)),
                (
                    "player_team_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bpl_app.teamsinfo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Matches",
            fields=[
                ("team1_id", models.CharField(max_length=128, unique=True)),
                ("team2_id", models.CharField(max_length=128, unique=True)),
                ("status", models.CharField(max_length=128)),
                (
                    "match_no",
                    models.CharField(
                        max_length=12, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "umpire_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bpl_app.umpires",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CriketScores",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("runs", models.IntegerField()),
                ("wickets", models.IntegerField()),
                ("status", models.CharField(max_length=128)),
                (
                    "cmatch_no",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bpl_app.matches",
                    ),
                ),
            ],
        ),
    ]