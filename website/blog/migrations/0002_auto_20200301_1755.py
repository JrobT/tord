# Generated by Django 3.0.3 on 2020-03-01 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(name="post", options={"ordering": ["-posted"]},),
    ]
