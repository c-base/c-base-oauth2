import pytest
from django.contrib.auth import get_user_model
from django.utils import timezone


@pytest.mark.django_db
def test_user_create():
    get_user_model().objects.create(
        username="test",
        email="test@example.org",
        real_name="",
        is_temporary_alien=False
    )
    assert get_user_model().objects.count() == 1


@pytest.mark.django_db
def test_user_str():
    alien = get_user_model().objects.create(
        username="xenomorph",
        email="test@example.org",
        is_temporary_alien=True,
        valid_until=timezone.now()
    )
    assert str(alien) == 'xenomorph [ALIEN]'
