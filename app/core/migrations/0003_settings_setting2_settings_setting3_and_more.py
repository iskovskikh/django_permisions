# Generated by Django 4.0.6 on 2022-07-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_singletonsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='setting2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='settings',
            name='setting3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='singletonsettings',
            name='setting2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='singletonsettings',
            name='setting3',
            field=models.BooleanField(default=False),
        ),
    ]
