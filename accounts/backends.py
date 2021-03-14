from django.contrib.auth.backends import ModelBackend
from accounts.models import Accounts as User


class PasswordlessAuthBackend(ModelBackend):
    """Log in to Django without providing a password.

    """
def authenticate(self, mob=None):
        try:
            return User.objects.get(mob=mob)
        except User.DoesNotExist:
            return None

def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None