# Generated by Django 4.2.13 on 2024-07-14 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cafe", "0010_alter_cafe_thumbnail_image"),
    ]

    operations = [
        migrations.RemoveField(model_name="cafe", name="thumbnail_image_url",),
    ]
