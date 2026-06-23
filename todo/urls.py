from django.urls import path
from . import views
from . import templates

urlpatterns = [
    path("login.html/",templates.login),
    path("register.html/",templates.register),
    path("dashboard.html/",templates.dashboard),


    path("tasks/",views.Todoaddpost.as_view()),
    path("tasks/<int:pk>/",views.Todoobject.as_view())
]

