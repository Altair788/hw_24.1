# Generated by Django 4.2.2 on 2024-11-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0011_delete_coursepayment"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
