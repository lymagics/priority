from rest_framework import serializers

from ..models import Task
from users.api.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    """
    DRF serializer to represent Task model.
    """
    user = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'description', 'is_done', 'user', 'priority']
        read_only_fields = ['id']
