from django.core.cache import cache
from rest_framework.permissions import BasePermission
from .models import Permission


def get_permission_list(user):
    """
    获取权限列表,可用redis存取
    """
    # print(user.is_superuser)
    if user.is_superuser:
        perms_list = ['admin']
    else:
        perms = Permission.objects.none()
        roles = user.roles.all()
        if roles:
            for i in roles:
                perms = perms | i.perms.all()
        perms_list = perms.values_list('method', flat=True)
        perms_list = list(set(perms_list))
    cache.set(user.username + '__perms', perms_list, 60 * 60)
    return perms_list


class RbacPermission(BasePermission):
    """
    基于角色的权限校验类
    """

    def has_permission(self, request, view):
        """
        权限校验逻辑
        :param request:
        :param view: 视图对象
        :return:
        """
        path = request._request.path  # client访问的api接口名
        perms = get_permission_list(request.user)  # list
        if perms:
            if not hasattr(view, 'perms_map'):
                return True
            else:
                if path in perms:
                    return True
                else:
                    return False
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if not request.user:
            return False
        return True
