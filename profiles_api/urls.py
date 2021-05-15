from django.urls import path
from profiles_api import views

urlpatterns = [
    path('home/', views.HelloApiView.as_view()),
]