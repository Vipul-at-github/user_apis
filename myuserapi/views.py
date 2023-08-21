from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Url to create new user


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING),
        'password': openapi.Schema(type=openapi.TYPE_STRING, format='password'),
    }
))
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        username = request.data.get('username')
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        # user.save()
        token = Token.objects.create(user=user)
        data = {}
        data['token'] = token.key
        return Response(data)

# Url only accessible by authenticated users


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def protect(request):
    user = request.user
    token = Token.objects.get(user=user)
    data = {
        'username': user.username,
        'first_name': user.first_name,
        'token': token.key,
    }
    return Response(data)

# Url to logout user


@api_view(['GET'])
@csrf_exempt
@authentication_classes([TokenAuthentication])
def logout(request):
    '''Deletes authentication token'''
    request.user.auth_token.delete()
    return Response({'success': 'Logged out successfully'})


# Url to delete user
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def deleteuser(request):
    user = request.user
    user.delete()
    return Response({'success': 'User deleted successfully'})


# Url to update username of user with respective token
@swagger_auto_schema(
    method='put', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, format='username'),
        }
    ),
    # security=[{"Authorization": [], }],
)
@api_view(['PUT'])  # Allow PUT requests
# Only token authenticated users can access
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])  # Only authenticated users can update
def updateuser(request):
    user = request.user
    user.username = request.data.get('username', user.username)
    user.save()
    return Response({'message': 'User details updated successfully.'})
