# Generated by Django 3.2.9 on 2021-12-11 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0002_notification_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='status',
            field=models.CharField(choices=[('IN PROGRESS', 'In Progress'), ('Failed', 'Failed'), ('Completed', 'Completed')], default='IN PROGRESS', help_text='Current status of the send notification task', max_length=120),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='is_active',
            field=models.BooleanField(default=True, help_text='subscriber is actively receiving the notifications when sent'),
        ),
    ]
