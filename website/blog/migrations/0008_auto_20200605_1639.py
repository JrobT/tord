# Generated by Django 3.0.3 on 2020-06-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_auto_20200605_1634"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
