from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminForCreateDelete(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if getattr(view,'action',None) in ('create','destroy'):
            return bool(request.user and request.user.is_staff)

        return True
