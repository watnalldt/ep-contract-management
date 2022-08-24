from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def client_manager_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="/users/login"
):
    """
    Decorator for views that checks that the user logging in is a client manager,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_client_manager,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def account_manager_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="/users/login/"
):
    """
    Decorator for views that checks that the user logging in is an account manager,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_account_manager,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
