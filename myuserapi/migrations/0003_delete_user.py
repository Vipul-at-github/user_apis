# Generated by Django 4.1.5 on 2023-08-09 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myuserapi', '0002_delete_user_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
