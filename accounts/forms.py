from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Accounts


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Accounts
        fields = ('mob',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Accounts
        fields = ('mob',)