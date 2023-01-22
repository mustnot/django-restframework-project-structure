from .base import *


DEBUG = True

# Environment
ENVIRONMENT = "development"

# Application definition
INSTALLED_APPS += [
    "silk",
    "drf_yasg",
]

MIDDLEWARE += [
    "silk.middleware.SilkyMiddleware",
]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DATABASE_NAME", default="postgres"),
        "USER": env("DATABASE_USER", default="postgres"),
        "PASSWORD": env("DATABASE_PASSWORD", default="postgres"),
        "HOST": env("DATABASE_HOST", default="localhost"),
        "PORT": env("DATABASE_PORT", default=5432),
    }
}
