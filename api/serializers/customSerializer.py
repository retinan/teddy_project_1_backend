from allauth.account.utils import (filter_users_by_email, user_pk_to_url_str, user_username)
from allauth.utils import build_absolute_uri
from allauth.account.adapter import get_adapter
from allauth.account.forms import default_token_generator
from allauth.account import app_settings
from dj_rest_auth.forms import AllAuthPasswordResetForm
from dj_rest_auth.serializers import PasswordResetSerializer
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import serializers


class CustomAllAuthPasswordResetForm(AllAuthPasswordResetForm):

    def clean_email(self):
        """
        Invalid email should not raise error, as this would leak users
        for unit test: test_password_reset_with_invalid_email
        """
        email = self.cleaned_data["email"]
        email = get_adapter().clean_email(email)
        self.users = filter_users_by_email(email, is_active=True)
        return self.cleaned_data["email"]

    def save(self, request, **kwargs):
        current_site = get_current_site(request)
        email = self.cleaned_data['email']
        token_generator = kwargs.get('token_generator', default_token_generator)

        for user in self.users:
            temp_key = token_generator.make_token(user)

            path = f"127.0.0.1:3000/{user_pk_to_url_str(user)}/{temp_key}/"
            url = build_absolute_uri(request, path)
            #Values which are passed to password_reset_key_message.txt
            context = {
                "current_site": '127.0.0.1:3000',
                "user": user,
                "password_reset_url": '127.0.0.1:3000',
                "request": request,
                "path": path,
                "domain": '127.0.0.1:3000'
            }

            if app_settings.AUTHENTICATION_METHOD != app_settings.AuthenticationMethod.EMAIL:
                context['username'] = user_username(user)
            get_adapter(request).send_mail(
                'account/email/password_reset_key', email, context
            )

        return self.cleaned_data['email']


class MyPasswordResetSerializer(PasswordResetSerializer):

    def validate_email(self, value):
        # use the custom reset form
        self.reset_form = CustomAllAuthPasswordResetForm(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)

        return value