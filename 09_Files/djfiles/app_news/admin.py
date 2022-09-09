from django.contrib import admin
from app_news.models import News, Comment, Tegs
from app_users.models import Profile


class CommentInLine(admin.TabularInline):
    model = Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'create_date', 'id', ]
    search_fields = ['text', ]
    inlines = [CommentInLine]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', '__str__']
    list_filter = ['user_name', 'user']

    actions = ['removed_by_admin']

    def removed_by_admin(self, request, queryset):
        queryset.update(comment_text='Removed by admin', user_name='')

    removed_by_admin.short_description = 'Removed by admin'


class TegsAdmin(admin.ModelAdmin):

    list_display = ['name']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_verification', ]


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tegs, TegsAdmin)
admin.site.register(Profile, ProfileAdmin)

