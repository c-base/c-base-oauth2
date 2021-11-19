from django.urls import reverse, resolve


def test_user_profile_reverse():
    "user_profile_api should reverse to /oauth/user/profile/."
    assert reverse('user_profile_api') == '/oauth/user/profile/'


def test_user_profile_resolve():
    "/oauth/user/profile/ should resolve to user_profile_api."
    assert resolve('/oauth/user/profile/').view_name == 'user_profile_api'