from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение, позволяющее только владельцу объекта редактировать его.
    Запросы GET, HEAD и OPTIONS разрешены всем.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        if request.method == 'POST':
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
