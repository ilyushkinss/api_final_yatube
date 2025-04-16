from rest_framework import permissions


# class IsAuthorOrReadOnly(permissions.BasePermission):
#     message = 'Запрещено изменять чужой контент!'

#     def has_object_permission(self, request, view, obj):
#         if not (
#             request.method in permissions.SAFE_METHODS
#             or request.user == obj.author
#         ):
#             return False
#         return True


# class ReadOnly(permissions.BasePermission):

#     def has_permission(self, request, view):
#         return request.method in permissions.SAFE_METHODS
class IsAuthorOrReadOnly(permissions.BasePermission):
    message = 'Нельзя изменять чужой контент!'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.author == request.user
