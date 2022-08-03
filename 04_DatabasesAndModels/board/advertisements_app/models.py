from django.db import models


class Advertisement(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=1000, db_index=True)
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена', default=0)
    publication_date = models.DateTimeField(auto_now=True)
    stop_publication = models.DateTimeField(verbose_name='Дата окончания публикации')
    type = models.CharField(max_length=100, verbose_name='Тип объявления', default='Продажа')

    user_status = models.ForeignKey('User', default=None, null=True, on_delete=models.CASCADE)
    category_status = models.ForeignKey('Category', default=None, null=True,
                                        on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements'
        ordering = ['title']


class AdvertisementCategoryStatus(models.Model):
    name = models.CharField(max_length=100)


class AdvertisementUserStatus(models.Model):
    name = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.IntegerField(verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='E-mail')
    new_status = AdvertisementUserStatus(name=name)
    new_status.save()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    new_category = AdvertisementCategoryStatus(name=name)
    new_category.save()

    def __str__(self):
        return self.name


