from rest_framework import permissions

class UpadateOwnProfile(permissions.BasePermission):
    """ update their own profile"""
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnstatus(permissions.BasePermission):
    """ allow user to Update their own status"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
