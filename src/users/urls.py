from django.urls import path

from .api.views import UserListCreateAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserRetrieveUpdateAPIView.as_view(), name='users-detail'),
]

app_name = 'users'
