# Generated by Django 4.0.6 on 2022-08-19 07:36

import birthday.fields
import datetime
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_alter_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=birthday.fields.BirthdayField(blank=True, default=datetime.datetime(2022, 8, 19, 13, 6, 8, 82093)),
        ),
    ]
