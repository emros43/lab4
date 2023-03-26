from django.contrib import admin
from .models import Question, Choice

class CommentInline(admin.StackedInline):
    model = Choice
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Question, PostAdmin)
