from django.contrib import admin
from .models import Review, Course


# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    fields = ['course', 'name', 'email', 'comment', 'rating', 'created_at']


class CourseAdmin(admin.ModelAdmin):
    fields = ['title', 'url']


admin.site.register(Review, ReviewAdmin)
admin.site.register(Course, CourseAdmin)
