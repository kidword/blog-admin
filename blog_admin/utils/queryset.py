def get_child_queryset2(obj, hasParent=True):
    '''
    获取所有子集
    obj实例
    数据表需包含parent字段
    是否包含父默认True
    '''
    cls = type(obj)
    queryset = cls.objects.none()
    fatherQueryset = cls.objects.filter(pk=obj.id)
    if hasParent:
        queryset = queryset | fatherQueryset
    child_queryset = cls.objects.filter(parent=obj)
    while child_queryset:
        queryset = queryset | child_queryset
        child_queryset = cls.objects.filter(parent__in=child_queryset)
    return queryset
