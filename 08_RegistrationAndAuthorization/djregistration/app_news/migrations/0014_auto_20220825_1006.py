# Generated by Django 2.2 on 2022-08-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0013_auto_20220822_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активность'),
        ),
    ]
