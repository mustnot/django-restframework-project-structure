from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path("api/v1/", include("api.v1.urls")),
]

if settings.ENVIRONMENT == "development":
    schema_view = get_schema_view(
        openapi.Info(
            title="API",
            default_version="v1",
            description="API",
            terms_of_service="https://www.google.com/policies/terms/",
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )

    urlpatterns += [
        path("silk/", include("silk.urls", namespace="silk")),
        path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
        path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    ]
