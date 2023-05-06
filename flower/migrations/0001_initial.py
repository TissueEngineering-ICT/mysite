# Generated by Django 4.1.7 on 2023-04-05 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("picture", models.ImageField(upload_to="images/")),
                ("title", models.CharField(default="picture", max_length=200)),
                ("first_name", models.CharField(default="", max_length=20)),
                ("second_name", models.CharField(default="", max_length=20)),
                ("third_name", models.CharField(default="", max_length=20)),
                ("fourth_name", models.CharField(default="", max_length=20)),
                ("fifth_name", models.CharField(default="", max_length=20)),
                ("first_value", models.FloatField(default=0)),
                ("second_value", models.FloatField(default=0)),
                ("third_value", models.FloatField(default=0)),
                ("fourth_value", models.FloatField(default=0)),
                ("fifth_value", models.FloatField(default=0)),
            ],
        ),
    ]
