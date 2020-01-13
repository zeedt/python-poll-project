from django.contrib import admin
from .models import Question, Choice, User
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['question', 'choice_text', 'votes']

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'first_name']


admin.site.register(Question, QuestionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Choice, ChoiceAdmin)
