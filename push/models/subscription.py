from django.db import models


class Subscription(models.Model):
    endpoint = models.URLField(max_length=500, blank=False, null=False, unique=True)
    public_key = models.CharField(max_length=200, blank=False, null=False)
    auth_key = models.CharField(max_length=200, blank=False, null=False)
    subscribe_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(
        default=True,
        help_text="subscriber is actively receiving the notifications when sent"
    )

    def __str__(self):
        return str(self.endpoint)

