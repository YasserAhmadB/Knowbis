# Generated by Django 3.2 on 2022-01-17 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_auto_20211216_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='creation_time',
            field=models.TimeField(null=True),
        ),
    ]
