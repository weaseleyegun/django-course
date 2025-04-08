from rest_framework.serializers import ModelSerializer
from .models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__" #Models에 존재하느 field들을 모두 가져옴
        