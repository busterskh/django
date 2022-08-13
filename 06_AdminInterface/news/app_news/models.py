from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.CharField(max_length=10000, verbose_name='Текст статьи')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    change_date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    is_active = models.BooleanField(verbose_name='Активность', default=True)

    class Meta:
        db_table = 'News'
        ordering = ['-create_date', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])


class Comment(models.Model):
    user_name = models.CharField(max_length=20, verbose_name='Имя пользователя')
    comment_text = models.CharField(max_length=1000, verbose_name='Текст комментария')
    create_comment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Comments'
        ordering = ['-create_comment_date']

    def __str__(self):
        if len(self.comment_text) > 15:
            return f'{self.comment_text[:16]}...'
        return self.comment_text
