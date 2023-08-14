from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication


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


@api_view(['GET'])
@csrf_exempt
@authentication_classes([TokenAuthentication])
def logout(self, request, *args, **kwargs):
    '''Deletes authentication token'''
    request.user.auth_token.delete()
    return Response({'success': 'Logged out successfully'})


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def deleteuser(request):
    user = request.user
    user.delete()
    return Response({'success': 'User deleted successfully'})


@api_view(['PUT'])  # Allow PUT requests
@permission_classes([IsAuthenticated])  # Only authenticated users can update
def updateuser(request):
    user = request.user
    user.username = request.data.get('username', user.username)
    user.save()
    return Response({'message': 'User details updated successfully.'})
