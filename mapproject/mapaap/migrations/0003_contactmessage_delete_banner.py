# Generated by Django 4.2.4 on 2023-09-15 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mapaap", "0002_banner"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactMessage",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Banner",
        ),
    ]
