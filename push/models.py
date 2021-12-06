from django.db import models


# Create your models here.
class Subscription(models.Model):
    endpoint = models.URLField(max_length=200, blank=False, null=False, unique=True)
    public_key = models.CharField(max_length=200, blank=False, null=False)
    auth = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return str(self.endpoint)


class Notification(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    message = models.CharField(max_length=500, blank=False, null=False)
    action_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} || {self.message}"
