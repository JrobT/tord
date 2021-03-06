# Generated by Django 3.0.3 on 2020-06-03 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_auto_20200531_2047"),
    ]

    operations = [
        migrations.CreateModel(
            name="Email",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="active",
            field=models.BooleanField(
                default=False,
                help_text="Has this post been published?",
                verbose_name="Is Active",
            ),
        ),
    ]
