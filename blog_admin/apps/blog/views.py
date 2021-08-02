from django.shortcuts import render

# Create your views here.

import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.system.permission import get_permission_list
from utils.queryset import get_child_queryset2
from .models import Article
from rest_framework.permissions import IsAuthenticated
from .serializers import BlogListSerializer, BlogCreateSerializer, BlogModifySerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class BlogViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = BlogListSerializer

    def get_queryset(self):
        queryset = self.queryset
        # if hasattr(self.get_serializer_class(), 'setup_eager_loading'):
        #     queryset = self.get_serializer_class().setup_eager_loading(queryset)  # 性能优化
        return queryset

    def get_serializer_class(self):
        # 根据请求类型动态变更serializer
        if self.action == 'create':
            return BlogCreateSerializer
        elif self.action == 'list':
            return BlogListSerializer
        return BlogModifySerializer

