from django import template
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, EmailMultiAlternatives, send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

User = get_user_model()


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    plaintext = template.loader.get_template(
                        "passwords/password_reset_email.txt"
                    )
                    htmltemp = template.loader.get_template(
                        "passwords/password_reset_email.html"
                    )
                    c = {
                        "email": user.email,
                        "domain": "127.0.0.1:8000",
                        "site_name": "Website",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    text_content = plaintext.render(c)
                    html_content = htmltemp.render(c)
                    try:
                        msg = EmailMultiAlternatives(
                            subject,
                            text_content,
                            "Website <admin@example.com>",
                            [user.email],
                            headers={"Reply-To": "admin@example.com"},
                        )
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    messages.success(
                        request, "Password reset instructions have been emailed to you"
                    )
                    return redirect("pages:home")
    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name="passwords/password_reset.html",
        context={"password_reset_form": password_reset_form},
    )


class HTMLTitleMixin:
    html_title = ""
    html_title_prefix = "EP | "
    html_title_suffix = ""
    html_title_required = True

    def get_html_title(self):
        """Return the class title attr by default,
        but can customize this by overriding"""
        return self.html_title

    def get_html_title_required(self):
        return self.html_title_required

    def get_html_title_prefix(self):
        return self.html_title_prefix

    def get_html_title_suffix(self):
        return self.html_title_suffix

    def generate_html_title(self):
        title = self.get_html_title()

        if not title and self.get_html_title_required():
            raise ValueError("HTMLTitleMixin requires an html_title")

        return self.get_html_title_prefix() + title + self.get_html_title_suffix()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["html_title"] = self.generate_html_title()
        return context
