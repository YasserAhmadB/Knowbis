# Generated by Django 3.2 on 2021-12-18 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
