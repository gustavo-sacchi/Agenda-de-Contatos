# Generated by Django 3.2.7 on 2021-10-09 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpersonalizado',
            old_name='bio',
            new_name='Biografia',
        ),
    ]