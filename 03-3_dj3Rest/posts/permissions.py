from rest_framework import permissions

# Create a Custom Permission Class
# extend of `BasePermission`
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        # Read-Only Permissions for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions allowed to the Author
        return obj.author == request.user
