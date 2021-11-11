from django.urls import path
from .views import Courses, CourseById, RegistrationCourse

urlpatterns = [
    path('courses/<int:course_id>/registrations/', RegistrationCourse.as_view()),
    path('courses/', Courses.as_view()),
    path('courses/<int:course_id>/', CourseById.as_view()) 
]
