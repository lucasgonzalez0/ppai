# Generated by Django 4.0.5 on 2022-07-04 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recurso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='reservable',
            field=models.BooleanField(default=False),
        ),
    ]