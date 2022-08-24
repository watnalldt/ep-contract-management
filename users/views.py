from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_control


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd["username"], password=cd["password"])

            if user is not None:
                login(request, user)
                if user.is_authenticated and user.is_client_manager:
                    return redirect(
                        "client_managers:dashboard"
                    )  # Go to client dashboard
                elif user.is_authenticated and user.is_account_manager:
                    return redirect(
                        "account_managers:dashboard"
                    )  # Go to account manager dashboard
            else:
                messages.error(request, "Invalid username or password.")
    else:
        # Invalid email or password. Handle as you wish
        form = AuthenticationForm()

    return render(request, "registration/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("users:login")
