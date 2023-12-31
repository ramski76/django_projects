# Generated by Django 4.2.6 on 2023-10-11 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('chat', '0002_rename_creator_chatrooms_created_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chatrooms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.useraccounts')),
            ],
        ),
    ]
