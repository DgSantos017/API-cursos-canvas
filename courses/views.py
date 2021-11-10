from django.contrib.auth.models import User
from accounts.permissions import Instructor
from .models import Course
from .serializers import CourseSerializer
from django.db.utils import IntegrityError

from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Courses(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def post(self, request):
        try:
            name = request.data['name']
            course = Course.objects.create(name=name)
            serializer = CourseSerializer(course)
            return Response(serializer.data, status=201)

        except IntegrityError:
            return Response({"error": "Course with this name already exists"}, status=400)
        except KeyError as e:
            return Response({"error": f"{str(e)} is missing"})
        
    
