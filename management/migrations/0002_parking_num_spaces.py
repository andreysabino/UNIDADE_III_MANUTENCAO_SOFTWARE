# Generated by Django 4.2.3 on 2024-04-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="parking",
            name="num_spaces",
            field=models.IntegerField(default=0),
        ),
    ]
