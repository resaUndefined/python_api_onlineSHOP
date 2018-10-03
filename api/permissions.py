from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        if request.user.is_staff:
        	return True
        elif request.method in permissions.SAFE_METHODS:
        	return True
        return False