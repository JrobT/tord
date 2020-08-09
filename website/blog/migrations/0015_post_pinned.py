# Generated by Django 3.0.7 on 2020-07-25 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0014_tag_background"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="pinned",
            field=models.BooleanField(
                default=False,
                help_text="Has this post been pinned?",
                verbose_name="Is Pinned",
            ),
        ),
    ]
