from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    ReadOnlyPasswordHashField,
)
from django.core.exceptions import ValidationError

from apps.models.account_model import User


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    # (注意)Emailです。
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={"autofocus": True}),
        label="ユーザー名",
    )
    password = forms.CharField(
        label="パスワード",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    class Meta:
        model = User
        fields = ("username", "password")


# Admin用
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email", "user_name", "date_of_birth"]

    def clean_password_confirm(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise ValidationError("Passwords don't match")
        return password_confirm

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


# Admin用
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "user_name",
            "date_of_birth",
            "is_active",
            "is_admin",
        ]
