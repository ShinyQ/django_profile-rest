from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-view', views.HelloViewSet, basename='hello-view')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('home/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]