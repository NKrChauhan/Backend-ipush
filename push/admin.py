from django.contrib import admin
from .models import Subscriptions, Notifications


class NotificationSentTime(admin.ModelAdmin):
    readonly_fields = ('notification_sent_time',)


admin.site.register(Notifications,NotificationSentTime)


class SubscriptionTime(admin.ModelAdmin):
    readonly_fields = ('subscribe_time',)


admin.site.register(Subscriptions,SubscriptionTime)
