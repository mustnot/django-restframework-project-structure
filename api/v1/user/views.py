from rest_framework import generics
from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class UserListAPIView(generics.ListAPIView):
    class UserOutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ["id", "email", "role"]

    queryset = User.objects.all()
    serializer_class = UserOutputSerializer
