from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        read_only_fields = ["owner"]
        
    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

class TodoObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        