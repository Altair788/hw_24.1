# Generated by Django 4.2.2 on 2024-10-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0002_alter_lesson_link_video_alter_lesson_title"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="lesson",
            constraint=models.UniqueConstraint(
                fields=("title", "course"), name="unique_title_per_course"
            ),
        ),
    ]
