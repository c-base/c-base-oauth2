from django.urls import reverse, resolve


def test_user_profile_reverse():
    "user-profile should reverse to /oauth/user/profile/."
    assert reverse('user-profile') == '/oauth/user/profile/'


def test_user_profile_resolve():
    "/oauth/user/profile/ should resolve to user-profile."
    assert resolve('/oauth/user/profile/').view_name == 'user-profile'