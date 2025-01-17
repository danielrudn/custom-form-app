from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.CASCADE)

    express_consent = models.BooleanField(
        verbose_name="Express Consent",
    )
    marketing_opt_in = models.BooleanField(
        verbose_name="Marketing Opt In",
        default=False,
    )
