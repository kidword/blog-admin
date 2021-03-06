import re

from .models import User, Role, Organization, Permission
from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):
    """
    用户列表序列化
    """
    dept_name = serializers.StringRelatedField(source='dept')
    roles_name = serializers.StringRelatedField(source='roles', many=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'phone', 'email', 'position',
                  'username', 'is_active', 'date_joined', 'dept_name', 'dept', 'roles', 'avatar', 'roles_name']

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.select_related('superior', 'dept')
        queryset = queryset.prefetch_related('roles', )
        return queryset


class UserCreateSerializer(serializers.ModelSerializer):
    """
    创建用户序列化
    """
    username = serializers.CharField(required=True)
    phone = serializers.CharField(max_length=11, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'phone', 'email', 'dept',
                  'position', 'avatar', 'is_active', 'roles']

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise serializers.ValidationError(username + ' 账号已存在')
        return username

    def validate_phone(self, phone):
        re_phone = '^1[358]\d{9}$|^147\d{8}$|^176\d{8}$'
        if not re.match(re_phone, phone):
            raise serializers.ValidationError('手机号码不合法')
        if User.objects.filter(phone=phone):
            raise serializers.ValidationError('手机号已经被注册')
        return phone


class UserModifySerializer(serializers.ModelSerializer):
    """
    用户编辑序列化
    """
    phone = serializers.CharField(max_length=11, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'phone', 'email', 'dept',
                  'position', 'avatar', 'is_active', 'roles', 'is_superuser']

    def validate_phone(self, phone):
        re_phone = '^1[358]\d{9}$|^147\d{8}$|^176\d{8}$'
        if not re.match(re_phone, phone):
            raise serializers.ValidationError('手机号码不合法')
        return phone


class RoleSerializer(serializers.ModelSerializer):
    """
    角色序列化
    """

    class Meta:
        model = Role
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    """
    组织架构序列化
    """
    type = serializers.ChoiceField(
        choices=Organization.organization_type_choices, default='部门')

    class Meta:
        model = Organization
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    """
    权限序列化
    """

    class Meta:
        model = Permission
        fields = '__all__'
