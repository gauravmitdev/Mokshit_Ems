# Generated by Django 4.0.6 on 2022-08-29 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('worklog', '0002_worklog_active_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worklog', to=settings.AUTH_USER_MODEL),
        ),
    ]
