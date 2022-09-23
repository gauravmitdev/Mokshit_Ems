# Generated by Django 4.0.6 on 2022-09-08 09:51

import birthday.fields
import datetime
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_alter_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=birthday.fields.BirthdayField(blank=True, default=datetime.datetime(2022, 9, 8, 15, 21, 32, 980033)),
        ),
    ]
