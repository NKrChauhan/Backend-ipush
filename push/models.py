from django.db import models


NOTIFICATION_STATUS_CHOICE = [
        ('In Progress', 'In Progress'),
        ('Failed', 'Failed'),
        ('Completed', 'Completed')
    ]


class Subscription(models.Model):
    """
    is_active: flag which determine if the subscription is still receiving the notifications and still subscribed
    """
    endpoint = models.URLField(max_length=500, blank=False, null=False, unique=True)
    public_key = models.CharField(max_length=200, blank=False, null=False)
    auth_key = models.CharField(max_length=200, blank=False, null=False)
    subscribe_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.endpoint)


class Notification(models.Model):
    """
    status: gives what is the current status of the notification sending task
    """
    title = models.CharField(max_length=200, blank=False, null=False)
    message = models.CharField(max_length=500, blank=False, null=False)
    action_link = models.URLField(blank=True, null=True)
    sent_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=NOTIFICATION_STATUS_CHOICE, max_length=120, default='In Progress')

    def __str__(self):
        return f"{self.id} {self.title} || {self.message}"
