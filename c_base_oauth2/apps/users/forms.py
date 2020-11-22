from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.utils import timezone


class AlienAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        now = timezone.now()
        user_model = get_user_model()
        try:
            user_model.objects.get(username=username, is_temporary_alien=True, valid_until__gte=now)
        except user_model.DoesNotExist:
            raise self.get_invalid_login_error()
        # If there is a valid alien user just to the rest of the normal login flow.
        return super().clean()
