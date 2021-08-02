from .models import Article
from rest_framework import serializers


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    @staticmethod
    def setup_eager_loading(queryset):
        # select_related、prefetch_related 主要用于字段的外键查询
        """ Perform necessary eager loading of data. """
        queryset = queryset.select_related('superior', 'dept')
        queryset = queryset.prefetch_related('roles', )
        return queryset


class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def validate_username(self, username):
        if Article.objects.filter(username=username):
            raise serializers.ValidationError(username + ' 文章标题已存在')
        return username


class BlogModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
