from accounts.serializers import UserSerializer
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


class Register(APIView):
    def post(self, request):
        try:       
            username = request.data['username']
            password = request.data['password']
            is_staff = request.data['is_staff']
            is_superuser = request.data['is_superuser']

            user = User.objects.create_user(username=username, password=password, is_staff=is_staff, is_superuser=is_superuser)
            serializer = UserSerializer(user)
            user_serializer = {
                **serializer.data,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser
            }

            return Response(user_serializer, status=201)

        except KeyError as e:
            return Response({"error": f" is missing {str(e)}"}, status=400)

        except IntegrityError:
            return Response({"error": "user already exists"}, status=409)



class Login(APIView):
    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']

            user = authenticate(username=username, password=password)

            if user != None:
                token = Token.objects.get_or_create(user=user)[0]
                return Response({'token': token.key})
            
            return Response({"error": "Incorrect login or password"}, status=401)

        except KeyError as e:
            return Response({"error": f" is missing {str(e)}"})


