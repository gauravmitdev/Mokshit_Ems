# Generated by Django 4.0.6 on 2022-09-06 11:37

import birthday.fields
import datetime
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0039_alter_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=birthday.fields.BirthdayField(blank=True, default=datetime.datetime(2022, 9, 6, 17, 7, 35, 656596)),
        ),
    ]
