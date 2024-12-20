# Generated by Django 4.2.17 on 2024-12-17 17:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_collaboraterequest_remove_about_created_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
