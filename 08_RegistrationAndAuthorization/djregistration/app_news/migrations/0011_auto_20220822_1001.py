# Generated by Django 2.2 on 2022-08-22 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0010_auto_20220821_1312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-create_date'], 'permissions': (('can_publish', 'Может публиковать'),), 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
