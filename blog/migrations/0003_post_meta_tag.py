# Generated by Django 4.2.1 on 2023-05-17 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_title_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="meta_tag",
            field=models.CharField(default="", max_length=255),
        ),
    ]