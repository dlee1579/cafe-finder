# Generated by Django 4.2.13 on 2024-06-26 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cafe", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cafe",
            name="neighborhood",
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
