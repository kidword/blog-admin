from django.urls import path, include
from .views import UserViewSet, RoleViewSet, OrganizationViewSet, PermissionViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register('user', UserViewSet, basename="user")
router.register('role', RoleViewSet, basename="role")
router.register('organization', OrganizationViewSet, basename="organization")
router.register('permission', PermissionViewSet, basename="permission")

urlpatterns = [
    path('', include(router.urls)),
]

