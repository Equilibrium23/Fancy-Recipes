# Generated by Django 3.1.4 on 2021-05-14 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_account_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]
