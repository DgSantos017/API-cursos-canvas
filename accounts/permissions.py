from rest_framework.permissions import BasePermission


class Instructor(BasePermission):
    def permission(self, request, view):
        return request.user.is_superuser and request.user.is_staff


class Facilitator(BasePermission):
    def permission(self, request, view):
        return request.user.is_staff and not request.user.is_superuser


class Student(BasePermission):
    def permission(self, request, view):
        if request.user != 'AnonymousUser' and not request.user.is_superuser and not request.user.is_staff:
            return True

