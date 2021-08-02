from rest_framework import routers

from django.urls import path, include

router = routers.DefaultRouter()

router.register('user', BlogViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls)),
]
