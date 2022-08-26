# Generated by Django 2.2 on 2022-08-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0014_auto_20220825_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tegs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='teg',
            field=models.ForeignKey(default=None, null=True, on_delete=None, to='app_news.Tegs'),
        ),
    ]
