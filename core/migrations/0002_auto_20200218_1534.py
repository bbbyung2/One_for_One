# Generated by Django 2.2.9 on 2020-02-18 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='timer',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]