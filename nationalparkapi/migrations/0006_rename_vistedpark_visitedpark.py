# Generated by Django 4.1.1 on 2022-09-13 16:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nationalparkapi', '0005_image_alt_text_image_caption_image_credit_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VistedPark',
            new_name='VisitedPark',
        ),
    ]
