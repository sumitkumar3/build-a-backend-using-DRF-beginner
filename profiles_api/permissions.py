from rest_framework import Permissions

class UpadateOwnProfile(Permissions.BasePermission):
    """ update their own profile"""
    def object_has_permission(self, request, view, obj):

        if request.method is Permissions.SAFE_METHOD:
            return True

        return obj.id == request.user.id
