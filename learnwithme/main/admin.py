from django.contrib import admin
from .models import Category, Article, Comment, ReplyComment

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(ReplyComment)

