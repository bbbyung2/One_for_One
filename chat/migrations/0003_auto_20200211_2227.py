# Generated by Django 2.2.9 on 2020-02-11 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20200211_2217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='room',
            new_name='Room',
        ),
    ]