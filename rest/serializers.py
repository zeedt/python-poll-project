from rest_framework import serializers
from .models import Review, Course


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'email': {'write_only': True}}  # only receive from user and not sent to user
        fields = ('id', 'course', 'name', 'email', 'comment', 'rating', 'created_at')
        model = Review


class CourseSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(read_only=True, many=True)
    # Instead of showing reviews with the course, hyperlink can be used instead
    # reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='apiv2:review-detail')
    # primary key can be used instead as well
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        fields = ('id', 'title', 'url', 'reviews')
        model = Course
