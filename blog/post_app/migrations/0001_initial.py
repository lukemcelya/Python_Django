# Generated by Django 5.1.1 on 2024-09-24 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
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
                ("title", models.CharField(blank=True, max_length=100)),
                ("entry", models.TextField(max_length=500)),
                ("date", models.DateField()),
            ],
        ),
    ]