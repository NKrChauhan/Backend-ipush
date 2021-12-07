from django.db import models


class Subscription(models.Model):
    endpoint = models.URLField(max_length=500, blank=False, null=False, unique=True)
    public_key = models.CharField(max_length=200, blank=False, null=False)
    auth_key = models.CharField(max_length=200, blank=False, null=False)
    subscribe_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.endpoint)


class Notification(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    message = models.CharField(max_length=500, blank=False, null=False)
    action_link = models.URLField(blank=True, null=True)
    sent_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} || {self.message}"
