import json
from urllib.parse import urlencode

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth.views import LoginView
from oauth2_provider.views import ScopedProtectedResourceView
from oauth2_provider.views import AuthorizationView

from .forms import AlienAuthenticationForm


class UserProfileView(ScopedProtectedResourceView):
    """
    View that returns a user profile JSON object.
    The contents of the JSON depend on the scopes requested by the OAuth2
    client (e.g. the third-party service).
    """
    required_scopes = ['membership']

    def has_scope(self, request, scope):
        try:
            return scope in request.scopes
        except AttributeError:
            core = self.get_oauthlib_core()
            is_valid, _ = core.verify_request(request, scopes=[scope])
            return is_valid

    def get(self, request):
        # If access_token is supplied as a query param, there is a bug in Django-Oauth-Toolkit
        if not request.user.is_authenticated:
            access_token = request.GET.get('access_token', None)
            if access_token:
                core = self.get_oauthlib_core()
                uri, http_method, body, headers = core._extract_params(request)

                valid, r = core.server.verify_request(uri, http_method, body, headers, scopes=self.required_scopes)
                if valid:
                    request = r   # overwrite request with the sanitized / verified request
            else:
                raise HttpResponseForbidden()

        data = {
            "username": request.user.username,
            "display_name": request.user.username,
            'email': request.user.email,
            'uid_number': request.user.uid,   # May be null
        }
        
        if self.has_scope(request, 'email'):
            data['email'] = request.user.email

        if self.has_scope(request, 'groups'):
            data['groups'] = [str(group) for group in request.user.groups.all()]

        if self.has_scope(request, 'realname'):
            data['realname'] = f'{request.user.first_name} {request.user.last_name}'

        return HttpResponse(
            json.dumps(data, indent=2),
            content_type="application/json"
        )


class CustomAuthorizationView(AuthorizationView):
    """
    The AuthorizationView of django-oauth-toolkit does not work when
    the the `scope` parameter is empty. With some OAuth2 clients it
    is hard to change the `scope` parameter. We therefor use this
    shim view to do a redirect that adds default scopes when there is
    no `scope` given in the request to /oauth/authorize/.
    """
    def get(self, request, *args, **kwargs):
        if request.GET.get('scope', '') == '':
            query = {key: request.GET.get(key) for key in request.GET.keys()}
            query['scope'] = 'membership email'   # add extra scopes if none present
            url = f'{reverse("custom_authorize")}?{urlencode(query)}'
            return HttpResponseRedirect(url)
        # call regular /oauth/authorize
        return super().get(request, *args, **kwargs)


class AlienLoginView(LoginView):
    template_name = 'users/alien_login.html'
    # Same as Django's AuthenticationForm but also checks if your ALIEN account
    # is still valid.
    form_class = AlienAuthenticationForm
