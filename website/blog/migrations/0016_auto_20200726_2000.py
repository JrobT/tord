# Generated by Django 3.0.7 on 2020-07-26 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0015_post_pinned"),
    ]

    operations = [
        migrations.AlterModelOptions(name="post", options={"ordering": ["-posted"]},),
    ]