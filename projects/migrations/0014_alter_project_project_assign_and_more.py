# Generated by Django 4.0.6 on 2022-09-16 05:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0013_alter_project_project_assign_alter_tasks_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_assign',
            field=models.ManyToManyField(related_name='project_assign', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_controll_by',
            field=models.ManyToManyField(related_name='project_controll_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='task',
            field=models.ManyToManyField(related_name='project', to='projects.tasks'),
        ),
    ]
