from django.contrib import admin
from app_news.models import News, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date', 'is_active', 'id']
    list_filter = ['is_active']
    search_fields = ['title', 'text']
    inlines = [CommentInLine]

    actions = ['mark_as_active', 'mark_as_not_active']

    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_as_not_active(self, request, queryset):
        queryset.update(is_active=False)

    mark_as_active.short_description = 'Mark as active'
    mark_as_not_active.short_description = 'Mark as not active'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', '__str__']
    list_filter = ['user_name']

    actions = ['removed_by_admin']

    def removed_by_admin(self, request, queryset):
        queryset.update(comment_text='Removed by admin', user_name='')

    removed_by_admin.short_description = 'Removed by admin'


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
