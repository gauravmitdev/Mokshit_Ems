# Generated by Django 4.0.6 on 2022-07-29 07:44

import birthday.fields
import datetime
from django.db import migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_managers_user_dob_dayofyear_internal_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=birthday.fields.BirthdayField(blank=True, default=datetime.datetime(2022, 7, 29, 13, 14, 56, 234663)),
        ),
    ]
