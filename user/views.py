from django.shortcuts import render
from rest_framework import status

from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Create your views here.
class UserView(APIView):
    def get(self, request):
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        for user in user_serializer.data:
            user.pop('password')
        return Response({"users": user_serializer.data})

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        create_user = User.objects.create_user(username=username, password=password, email=email,
                                               first_name=first_name, last_name=last_name)
        if create_user:
            create_user.save()
            return Response({'Message':'User Created Successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Message':'User already exists'}, status=status.HTTP_200_OK)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        user = User.objects.filter(username=user).first()
        user_serializer = UserSerializer(user)
        if user_serializer.data:
            print(user_serializer.data)
            profile_details = ({'username': user_serializer.data.get('username'),
                                'email': user_serializer.data.get('email'),
                                'first_name': user_serializer.data.get('first_name'),
                                'last_name': user_serializer.data.get('last_name')})

            return Response(profile_details, status=status.HTTP_200_OK)
        else:
            return Response({'Message':'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

class UserSearchView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.data.get('user')
        user = User.objects.filter(username=user).first()
        user_serializer = UserSerializer(user)
        if user_serializer.data:
            user_id = user_serializer.data.get('id')
            return Response({"user_id": user_id})
        return Response({'Message':'User does not exist'}, status=status.HTTP_404_NOT_FOUND)