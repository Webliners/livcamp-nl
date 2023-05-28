# Generated by Django 4.2.1 on 2023-05-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_category_post_header_image_post_published_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_date']},
        ),
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]