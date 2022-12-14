# Generated by Django 2.2 on 2022-09-08 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0020_auto_20220908_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='blog_pic',
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img/')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_news.News')),
            ],
        ),
    ]
