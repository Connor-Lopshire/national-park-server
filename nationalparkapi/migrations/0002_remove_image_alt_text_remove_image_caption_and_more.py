# Generated by Django 4.1.1 on 2022-09-12 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nationalparkapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='alt_text',
        ),
        migrations.RemoveField(
            model_name='image',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='image',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
    ]
