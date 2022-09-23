# Generated by Django 4.0.6 on 2022-09-22 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_mokshit', '0017_gsk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.TextField()),
                ('b', models.TextField()),
                ('c', models.TextField()),
                ('d', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('check_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='admin_mokshit.check')),
                ('ids', models.IntegerField(primary_key=True, serialize=False)),
                ('e', models.TextField(null=True)),
            ],
            bases=('admin_mokshit.check',),
        ),
    ]
