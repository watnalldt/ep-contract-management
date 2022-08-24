from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views import defaults as default_views

from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="passwords/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="passwords/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("account_managers/", include("account_managers.urls")),
    path("clients/", include("clients.urls")),
    path("", include("pages.urls")),
]
if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]

    # Enable the debug toolbar only in DEBUG mode.
    if settings.DEBUG and settings.DEBUG_TOOLBAR:
        urlpatterns = [
            path("__debug__/", (include("debug_toolbar.urls")))
        ] + urlpatterns
