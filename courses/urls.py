from django.urls import path
from .views import Courses

urlpatterns = [
    path('courses/', Courses.as_view()),
]
