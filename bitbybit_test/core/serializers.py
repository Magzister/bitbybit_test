from rest_framework import serializers

from .models import CustomUser
from .models import Course
from .models import Grade


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('id', 'student', 'course', 'grade')


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'type')


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(type='Teacher'))
    students = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(type='Student'), many=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'teacher', 'students')
