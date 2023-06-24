from rest_framework.permissions import BasePermission

class OwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
        