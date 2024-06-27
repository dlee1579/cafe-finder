# Generated by Django 4.2.13 on 2024-06-26 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cafe", "0002_cafe_neighborhood"),
    ]

    operations = [
        migrations.AddField(
            model_name="cafe",
            name="has_wall_outlets",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="cafe",
            name="is_pet_friendly",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
