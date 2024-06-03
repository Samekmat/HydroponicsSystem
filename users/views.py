from typing import Type

from django.contrib.auth.models import User
from django.db.models import QuerySet
from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset: QuerySet[User] = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class: Type[UserSerializer] = UserSerializer
