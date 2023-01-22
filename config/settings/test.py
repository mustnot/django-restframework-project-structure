from .base import *

IS_TESTING = True

# Environment
ENVIRONMENT = "test"

ALLOWED_HOSTS = ["*"]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DATABASE_NAME", default="postgres_test"),
        "USER": env("DATABASE_USER", default="postgres"),
        "PASSWORD": env("DATABASE_PASSWORD", default="postgres"),
        "HOST": env("DATABASE_HOST", default="localhost"),
        "PORT": env("DATABASE_PORT", default=5432),
    }
}
