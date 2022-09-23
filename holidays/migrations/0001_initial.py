# Generated by Django 4.0.6 on 2022-08-01 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holidayname', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
