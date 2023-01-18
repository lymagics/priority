from django.urls import path, include

urlpatterns = [
    path('', include('users.urls')),
    path('', include('tokens.urls')),
    path('', include('tasks.urls')),
]

app_name = 'api'
