from rest_framework import serializers
from .models import Review, Course


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'email': {'write_only': True}} #only receive from user and not sent to user
        fields = ('id', 'course', 'name', 'email', 'comment', 'rating', 'created_at')
        model = Review


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'url')
        model = Course
