# Generated by Django 2.2 on 2022-08-29 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0017_auto_20220826_0722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['is_active'], 'permissions': (('create', 'Может публиковать'), ('edit', 'Может редактировать')), 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
