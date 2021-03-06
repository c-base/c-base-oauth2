"""c_base_oauth2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from .apps.users.views import UserProfileAPIView
from .apps.users.views import UserProfileView
from .apps.users.views import CustomAuthorizationView
from .apps.users.views import AlienLoginView


urlpatterns = [
    path('oauth/admin/', admin.site.urls),
    path('oauth/user/profile/', UserProfileAPIView.as_view(), name='user_profile_api'),
    path('oauth/accounts/profile/', UserProfileView.as_view(), name='user_profile'),
    path('oauth/accounts/alien_login/', AlienLoginView.as_view(), name="alien_login"),
    path('oauth/accounts/', include('django.contrib.auth.urls')),
    path('oauth/authorize/', CustomAuthorizationView.as_view(), name="custom_authorize"),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
