# Generated by Django 3.2 on 2021-12-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0002_auto_20211218_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('V', 'Verified'), ('B', 'Blocked')], default='A', max_length=1),
        ),
    ]
