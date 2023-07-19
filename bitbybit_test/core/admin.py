from django.contrib import admin

from .models import CustomUser, Course, Grade

admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Grade)
