from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreate.as_view()),
    path('', views.CommentListCreate.as_view()),
]

