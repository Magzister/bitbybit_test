from django.urls import path

from .views import CustomUserLoginView
from .views import CreateCourseView
from .views import GradeCreateView

urlpatterns = [
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path('create-course/', CreateCourseView.as_view(), name='create-course'),
    path('grades/', GradeCreateView.as_view(), name='create-grade'),
]
