"""
Production settings.

All environment-specific values come from environment variables / .env.
Required: DJANGO_SECRET_KEY, DJANGO_ALLOWED_HOSTS, DATABASE_URL.
"""

from .base import *  # noqa: F401,F403
from .base import env

DEBUG = False

# Required, no default: the app must not start with an open host list.
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env.list("DJANGO_CSRF_TRUSTED_ORIGINS", default=[])

# e.g. postgres://user:password@host:5432/dbname
DATABASES = {"default": env.db("DATABASE_URL")}

# HTTPS everywhere
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS: one year, including subdomains
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
