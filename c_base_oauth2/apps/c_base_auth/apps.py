from django.apps import AppConfig


class CBaseAuthConfig(AppConfig):
    name = 'c_base_oauth2.apps.c_base_auth'
    verbose_name = 'c-base Auth'

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
