from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Разрешаем только чтение и обновление (без создания/удаления)
    http_method_names = ['get', 'put', 'patch']
    permission_classes = [permissions.AllowAny]  # по заданию авторизация не требуется