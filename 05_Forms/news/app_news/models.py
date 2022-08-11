from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.CharField(max_length=10000, verbose_name='Текст статьи')
    create_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'News'
        ordering = ['-create_date', ]

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=20, verbose_name='Имя пользователя')
    comment_text = models.CharField(max_length=1000, verbose_name='Текст комментария')
    create_comment_date = models.DateTimeField(auto_now_add=True)
    news_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'Comments'
        ordering = ['-create_comment_date']

    def __str__(self):
        return self.user_name
