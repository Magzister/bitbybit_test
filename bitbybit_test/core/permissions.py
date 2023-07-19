from rest_framework.permissions import BasePermission


class IsTeacherForCourse(BasePermission):
    def has_permission(self, request, view):
        if request.user.type != 'Teacher':
            return False

        course_id = request.data.get('course')

        return request.user.teacher_courses.filter(id=course_id).exists()
