# Generated by Django 4.2.16 on 2024-11-22 19:00

import apps.blog.models
import core.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(storage=core.storage_backends.PublicMediaStorage(), upload_to=apps.blog.models.blog_thumbnail_directory),
        ),
    ]