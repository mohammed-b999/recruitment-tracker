"""Smoke tests: the project boots and core security settings are in place."""

import pytest
from django.conf import settings
from django.contrib.auth.hashers import get_hasher
from django.core.management import call_command


def test_system_check_passes():
    # Raises SystemCheckError if any error-level check fails.
    call_command("check", fail_level="ERROR")


@pytest.mark.django_db
def test_admin_login_page_loads(client):
    response = client.get("/admin/login/")
    assert response.status_code == 200


def test_argon2_is_default_password_hasher():
    assert get_hasher().algorithm == "argon2"
    assert settings.PASSWORD_HASHERS[0].endswith("Argon2PasswordHasher")
