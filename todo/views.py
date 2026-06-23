from django.shortcuts import render
from .serializer import TodoSerializer,TodoObjectSerializer
import datetime
from django.utils.timezone import now
from rest_framework.generics import (
    ListCreateAPIView,RetrieveUpdateDestroyAPIView
)
from .models import Todo
from .permissions import TodoPermision
from rest_framework.response import Response
from rest_framework import status

class Todoaddpost(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes =[TodoPermision]

    def get_queryset(self):
        today = self.request.query_params.get("today")
        allday = self.request.query_params.get("allday")
        if today:
            return Todo.objects.select_related("owner").filter(owner=self.request.user,start_time__date = now().date())
        elif allday:
            return Todo.objects.select_related("owner").filter(owner=self.request.user)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class Todoobject(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.select_related("owner")
    serializer_class = TodoObjectSerializer
    permission_classes = [TodoPermision]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.method == "PATCH":
            if instance.start_time.date() == now().date():
                if not instance.is_finished:
                    instance.is_finished = request.data.get("is_finished",True)
                    instance.end_time = now()
                    instance.save()
                    data=self.serializer_class(instance).data()
                    
                    return Response(data,status=status.HTTP_201_CREATED)
                return Response({"msg": "you only change when it false"})
            return Response({"msg": "you only change data , when data is now"})
        return Response({"msg": "you only accept patch method to update data"})
