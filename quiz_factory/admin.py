from django.contrib import admin

from quiz_factory.models import Category, Question, QuestionChoices

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(QuestionChoices)
