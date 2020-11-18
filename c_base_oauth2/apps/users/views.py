import json

from django.http import HttpResponse
from oauth2_provider.views import ScopedProtectedResourceView
from oauth2_provider.views.mixins import ScopedResourceMixin


class UserProfileView(ScopedProtectedResourceView):
    """
    View that returns a user profile JSON object.
    The contents of the JSON depend on the scopes requested by the OAuth2
    client (e.g. the third-party service).
    """
    required_scopes = ['membership']

    def has_scope(self, request, scope):
        core = self.get_oauthlib_core()
        is_valid, _ = core.verify_request(request, scopes=[scope])
        return is_valid

    def get(self, request):
        data = {
            "username": request.user.username,
            "display_name": request.user.username,
        }
        if self.has_scope(request, 'email'):
            data['email'] = request.user.email

        if self.has_scope(request, 'groups'):
            data['groups'] = ['crew', 'todo']

        if self.has_scope(request, 'realname'):
            data['realname'] = 'TODO'

        return HttpResponse(
            json.dumps(data, indent=2),
            content_type="application/json"
        )
