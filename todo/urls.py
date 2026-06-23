from django.urls import path
from . import views


urlpatterns = [
    path("tasks/",views.Todoaddpost.as_view()),
    path("tasks/<int:pk>/",views.Todoobject.as_view())
]

