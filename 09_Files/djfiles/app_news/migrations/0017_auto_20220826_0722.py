# Generated by Django 2.2 on 2022-08-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0016_auto_20220825_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tegs',
            name='news',
        ),
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.ManyToManyField(to='app_news.Tegs'),
        ),
    ]