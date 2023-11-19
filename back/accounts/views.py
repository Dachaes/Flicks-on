from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserInfoSerializer


# Create your views here.
@api_view(['GET'])
def get_user_info(requset, username):
    user = get_user_model()
    print(user.nickname)
    if requset.method == 'GET':
        serializer = UserInfoSerializer(user)
        return Response(serializer.data)