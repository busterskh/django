# Generated by Django 2.2 on 2022-08-03 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0005_remove_advertisement_count_view'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='advertisement',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(db_index=True, max_length=1000, verbose_name='Заголовок'),
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
    ]
