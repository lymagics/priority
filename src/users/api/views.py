from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import UserSerializer
from ..models import User
from ..permissions import IsProfileOwnerOrReadOnly
from core.mixins import PartialUpdateMixin


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateAPIView(PartialUpdateMixin, RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsProfileOwnerOrReadOnly,)
