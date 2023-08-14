from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.register, name='register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('protect/', views.protect, name='authorized'),
    path('logout/', views.logout, name='logout'),
    path('deleteuser/', views.deleteuser, name='deleteuser'),
    path('updateuser/', views.updateuser, name='updateuser')
]
