from django.db import models

IN_PROGRESS = 'IN PROGRESS'
FAILED = 'Failed'
COMPLETED = 'Completed'
NOTIFICATION_STATUS_CHOICE = [
        (IN_PROGRESS, 'In Progress'),
        (FAILED, 'Failed'),
        (COMPLETED, 'Completed')
    ]


class Notification(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    message = models.CharField(max_length=500, blank=False, null=False)
    action_link = models.URLField(blank=True, null=True)
    sent_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=NOTIFICATION_STATUS_CHOICE,
        max_length=120,
        default=IN_PROGRESS,
        help_text="Current status of the send notification task"
    )

    def __str__(self):
        return f"{self.id} {self.title} || {self.message}"
