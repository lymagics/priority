from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import TaskSerializer
from ..models import Task
from ..permissions import IsOwnerOrReadOnly
from core.mixins import PartialUpdateMixin


class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.select_related('user')
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskRetrieveUpdateDestroyAPIView(PartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.select_related('user')
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
