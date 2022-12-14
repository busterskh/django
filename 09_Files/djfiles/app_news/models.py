from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class News(models.Model):
    text = models.CharField(max_length=10000, verbose_name='Текст статьи')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    change_date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    tag = models.ForeignKey('Tegs', on_delete=None, default=None, null=True, blank=True)

    class Meta:
        db_table = 'News'
        ordering = ['create_date', ]
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        permissions = (
            ('create', 'Может публиковать'),
            ('edit', 'Может редактировать'),
        )

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])

    def short_text(self):
        if len(self.text) > 100:
            return self.text[:100] + '...'
        return self.text


class Comment(models.Model):
    user_name = models.CharField(max_length=20, verbose_name='Имя пользователя')
    comment_text = models.CharField(max_length=1000, verbose_name='Текст комментария')
    create_comment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Comments'
        ordering = ['-create_comment_date']

    def __str__(self):
        if len(self.comment_text) > 15:
            return f'{self.comment_text[:16]}...'
        return self.comment_text


class Tegs(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    img = models.ImageField(upload_to='img/')
    news = models.ForeignKey(News, on_delete=models.CASCADE)


