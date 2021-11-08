from accounts.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from .models import User

import django


class Register(APIView):
    def post(self, request):
        try:
            data_user = request.data
            user: User = User.objects.create_user(**data_user)
            serializer = UserSerializer(user)

            return Response(serializer.data, status=201)

        except django.db.utils.IntegrityError:
            return Response({"error": "user already exists"}, status=409)



class Login(APIView):
    def post(self, request):

        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)

        if not user:
            return Response({"error": "Incorrect login or password"}, status=401)

        token = Token.objects.get_or_create(user=user)[0]

        return Response({"token": token.key}, status=200)
