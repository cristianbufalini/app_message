# Generated by Django 5.0.1 on 2024-01-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("user", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
