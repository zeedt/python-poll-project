from rest_framework import serializers
from .models import Review, Course
from django.db.models import Avg


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'email': {'write_only': True}}  # only receive from user and not sent to user
        fields = ('id', 'course', 'name', 'email', 'comment', 'rating', 'created_at')
        model = Review

    def validate_rating(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError('Rating must be an integer between 1 and 5')


class CourseSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(read_only=True, many=True)
    # Instead of showing reviews with the course, hyperlink can be used instead
    # reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='apiv2:review-detail')
    # primary key can be used instead as well
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'title', 'url', 'reviews', 'average_rating')
        model = Course

    def get_average_rating(self, object):
        average = object.reviews.aggregate(Avg('rating')).get('rating__avg')
        if average is None:
            return 0
        return round(average * 2) / 2
