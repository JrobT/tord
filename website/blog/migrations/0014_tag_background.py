# Generated by Django 3.0.7 on 2020-07-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0013_auto_20200724_1338"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="background",
            field=models.CharField(db_index=True, default="#ffffff", max_length=7),
            preserve_default=False,
        ),
    ]