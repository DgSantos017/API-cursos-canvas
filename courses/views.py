from django.contrib.auth.models import User
from accounts.permissions import Instructor
from .models import Course
from .serializers import CourseSerializer
from django.db.utils import IntegrityError

from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegistrationCourse(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def put(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
            user_ids = request.data['user_ids']

            course.users.set([])

            for id in user_ids:
                user = User.objects.get(id=id)
                if user.is_staff or user.is_superuser:
                    return Response({"error": "Only students can be enrolled in the course"}, status=400)
                course.users.add(user)
            
            course.save()
            serializer = CourseSerializer(course)

            return Response(serializer.data)

        except Course.DoesNotExist:
            return Response({"error": "course does not exist"}, status=404)

        except User.DoesNotExist:
            return Response({"error": "invalid user_id list"}, status=404)

       
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
            return Response({"error": f"{str(e)} is missing"}, status=400)
    

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True) 
        return Response(serializer.data, status=200)


class CourseById(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Instructor]

    def put(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
            name = request.data['name']
            course.name = name
            course.save()
            serializer = CourseSerializer(course)

            return Response(serializer.data, status=200)
            
        except KeyError as e:
            return Response({"error": f"{str(e)} is missing"}, status=400)

        except Course.DoesNotExist:
            return Response({"error": "course does not exist"}, status=404)

        except IntegrityError:
            return Response({"error": "Course with this name already exists"}, status=400)


    def get(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
            serializer = CourseSerializer(course)
            return Response(serializer.data, status=200)

        except Course.DoesNotExist:
            return Response({"error": "course does not exist"}, status=404)

    def delete(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
            course.delete()

            return Response('', status=204)

        except Course.DoesNotExist:
            return Response({"error": "course does not exist"}, status=404)





        
    
