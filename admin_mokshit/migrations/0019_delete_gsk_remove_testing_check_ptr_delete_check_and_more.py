# Generated by Django 4.0.6 on 2022-09-22 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_mokshit', '0018_check_testing'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GSK',
        ),
        migrations.RemoveField(
            model_name='testing',
            name='check_ptr',
        ),
        migrations.DeleteModel(
            name='Check',
        ),
        migrations.DeleteModel(
            name='Testing',
        ),
    ]
