import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import ChatRooms, ChatMessages
from authentication.models import UserAccounts

# /////////////////////////////////////////////////////////////////////
# open routes

def index(request):
   
   authenticated = request.COOKIES.get("authenticated")
   if authenticated == "true":
       return render(request, 'home.html')
   else:
       return render(request, 'index.html')

# /////////////////////////////////////////////////////////////////////

def home(request):

    authenticated = request.COOKIES.get("authenticated")
    if authenticated == "true": 
        return render(request, 'home.html')
    else:
        return render(request, "login.html")
    
# open routes
# /////////////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////////////////////
# api routes
@csrf_exempt
def createroom(request):
    authenticated = request.COOKIES.get("authenticated")
    username = request.COOKIES.get("user")
    if authenticated == "true":
        if request.method == "POST":
            data = json.loads(request.body)
            if data:
                room_name = data.get('roomname')
                user_account = UserAccounts.objects.get(username=username)
                chat_room = ChatRooms(room_name=room_name, created_user=user_account)
                chat_room.save()
                return JsonResponse({"message" : "Room "+chat_room.room_name+ " created successfully"})
        else:
            return HttpResponse("Not Found")
    else:
        return HttpResponse("Not Found")


# /////////////////////////////////////////////////////////////////////

@csrf_exempt
def joinroom(request):
    authenticated = request.COOKIES.get("authenticated")
    username = request.COOKIES.get("user")
    if authenticated == "true":
        if request.method == "POST":
            data = json.loads(request.body)
            if data:
                room_name = data.get('roomname')
                user_account = UserAccounts.objects.get(username=username)
                try:
                    room = ChatRooms.objects.get(room_name=room_name)
                    room.members.add(user_account)
                    return JsonResponse({"message" : "Successfully joined Room "+room_name})
                except ChatRooms.DoesNotExist:
                    return JsonResponse({"message": "Room does not exist"})
            else:
                return JsonResponse({"message" : "Room does not exists"})
        else:
            return HttpResponse("Not Found")
    else:
        return HttpResponse("Not Found")
    
    

# /////////////////////////////////////////////////////////////////////

@csrf_exempt
def storemessages(request):
    authenticated = request.COOKIES.get("authenticated")
    username = request.COOKIES.get("user")
    if authenticated == "true":
        if request.method == "POST":
            message_data = json.loads(request.body)
            message_content = message_data.get("message")
            room_name = message_data.get("room")  
            user_account = UserAccounts.objects.get(username=username)
            room = ChatRooms.objects.get(room_name=room_name)
            chat_message = ChatMessages(user=user_account, room=room, message=message_content)
            chat_message.save()
            return JsonResponse({"message" : "Message Sent"})
        else:
            return HttpResponse("Not Found")
    else:
        return HttpResponse("Not Found")

# /////////////////////////////////////////////////////////////////////

@csrf_exempt
def returnrooms(request):
    authenticated = request.COOKIES.get("authenticated")
    username = request.COOKIES.get("user")
    if authenticated == "true":
        if request.method == "GET":
            user_account = UserAccounts.objects.get(username=username)
            created_rooms = ChatRooms.objects.filter(created_user=user_account)
            joined_rooms = ChatRooms.objects.filter(members=user_account)
            all_rooms = created_rooms | joined_rooms
            rooms_data = [{'room_name': room.room_name} for room in all_rooms]
            return JsonResponse({"user_rooms" : rooms_data})
        else:
            return HttpResponse("Not Found")
    else:
        return HttpResponse("Not Found")
    
# /////////////////////////////////////////////////////////////////////

@csrf_exempt
def returnmessages(request):
    authenticated = request.COOKIES.get("authenticated")
    if authenticated == "true":
        if request.method == "POST":
            message_data = json.loads(request.body)
            room_name = message_data.get("room")
            room = ChatRooms.objects.get(room_name=room_name)
            messages = ChatMessages.objects.filter(room=room)
            messages_data = [{'user': message.user.username, 'message': message.message} for message in messages]
            return JsonResponse({"messages" : messages_data})
        else:
            return HttpResponse("Not Found")
    else:
        return HttpResponse("Not Found")

# api routes
# /////////////////////////////////////////////////////////////////////