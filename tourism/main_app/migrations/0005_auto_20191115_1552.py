# Generated by Django 2.1.5 on 2019-11-15 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_session'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='check_in_date',
            new_name='check_in',
        ),
        migrations.RenameField(
            model_name='session',
            old_name='check_out_date',
            new_name='check_out',
        ),
    ]
