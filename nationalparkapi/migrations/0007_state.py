# Generated by Django 4.1.1 on 2022-09-21 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nationalparkapi', '0006_rename_vistedpark_visitedpark'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_code', models.CharField(max_length=2)),
            ],
        ),
    ]
