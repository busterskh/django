# Generated by Django 2.2 on 2022-08-20 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone_num',
            new_name='phone',
        ),
    ]
