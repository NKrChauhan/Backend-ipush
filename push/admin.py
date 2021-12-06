from django.contrib import admin
from .models import Subscription, Notification


class NotificationSentTime(admin.ModelAdmin):
    readonly_fields = ('sent_time',)


admin.site.register(Notification,NotificationSentTime)


class SubscriptionTime(admin.ModelAdmin):
    readonly_fields = ('subscribe_time',)


admin.site.register(Subscription,SubscriptionTime)
