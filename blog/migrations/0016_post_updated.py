# Generated by Django 4.2.1 on 2023-06-10 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateField(blank=True, null=True),
        ),
    ]
