# Generated by Django 4.2.7 on 2023-12-04 06:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projectsapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="image",
            field=models.FileField(blank=True, upload_to="project_images/"),
        ),
    ]
