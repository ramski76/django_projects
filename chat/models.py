from django.db import models
from authentication.models import UserAccounts


class ChatRooms(models.Model):

    room_name = models.CharField(max_length=100)
    created_user = models.ForeignKey(UserAccounts, on_delete=models.CASCADE)
    members = models.ManyToManyField(UserAccounts, related_name='group_members')

class ChatMessages(models.Model):

   user = models.ForeignKey(UserAccounts, on_delete=models.CASCADE)
   room = models.ForeignKey(ChatRooms, on_delete=models.CASCADE) 
   message = models.CharField(max_length=100000)
   timestamp = models.DateTimeField(auto_now_add=True)