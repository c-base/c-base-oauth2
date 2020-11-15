import pytest
from django.utils import timezone

from c_base_oauth2.apps.c_base_auth.models import TemporaryAlienAccount


@pytest.mark.django_db
def test_temporary_alien_account_create():
    TemporaryAlienAccount.objects.create(
        username='xenomorph',
        real_name="Alien aus Alien",
        valid_until=timezone.now()
    )
    assert TemporaryAlienAccount.objects.count() == 1


@pytest.mark.django_db
def test_temporary_alien_account_str():
    alien = TemporaryAlienAccount.objects.create(
        username='xenomorph',
        real_name="Alien aus Alien",
        valid_until=timezone.now()
    )
    assert str(alien) == 'xenomorph [ALIEN]'
