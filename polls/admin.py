from django.contrib import admin
from .models import Question, Choice, User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission, Group


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['question', 'choice_text', 'votes']

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'first_name', 'user_permissions']


class PermissionAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Question, QuestionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Permission,PermissionAdmin)
