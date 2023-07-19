from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )

    type = models.CharField(max_length=20, choices=USER_TYPES)

    class Meta:
        db_table = 'custom_user'


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(CustomUser, related_name='teacher_courses', on_delete=models.CASCADE, limit_choices_to={'type': 'Teacher'})
    students = models.ManyToManyField(CustomUser, related_name='Student_courses', limit_choices_to={'type': 'Student'})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'course'


class Grade(models.Model):
    GRADE_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
    )

    student = models.ForeignKey(CustomUser, related_name='student_grades', on_delete=models.CASCADE, limit_choices_to={'type': 'Student'})
    course = models.ForeignKey(Course, related_name='course_grades', on_delete=models.CASCADE)
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)

    def __str__(self):
        return f"{self.student} - {self.course}: {self.grade}"
    
    class Meta:
        db_table = 'grade'
