# Generated by Django 4.2.13 on 2024-06-26 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cafe", "0003_cafe_has_wall_outlets_cafe_is_pet_friendly"),
    ]

    operations = [
        migrations.AddField(
            model_name="cafe",
            name="thumbnail_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
