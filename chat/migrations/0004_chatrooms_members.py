# Generated by Django 4.2.6 on 2023-10-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('chat', '0003_chatmessages'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatrooms',
            name='members',
            field=models.ManyToManyField(related_name='group_members', to='authentication.useraccounts'),
        ),
    ]
