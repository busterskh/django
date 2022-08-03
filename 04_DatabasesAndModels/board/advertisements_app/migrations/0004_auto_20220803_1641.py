# Generated by Django 2.2 on 2022-08-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0003_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='count_view',
            field=models.IntegerField(auto_created=0, default=0),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='type',
            field=models.CharField(default='Продажа', max_length=100, verbose_name='Тип объявления'),
        ),
    ]
