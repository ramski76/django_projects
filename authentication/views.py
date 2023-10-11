from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import auth 
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .db.signup import checkIfUserExists, createUserAccount
from .db.login import checkCredentials
from django.template.loader import render_to_string
import json


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if data:
            username = data.get('username')
            password = data.get('password')
            boolean = checkCredentials(username=username, password=password)
            if boolean == True:
               html_content = render_to_string('home.html')
               response = HttpResponse(html_content, content_type='text/html')
               response.set_cookie('authenticated', 'true')
               response.set_cookie("user" , username)
               return response
            elif boolean == False:
                return JsonResponse({'message': 'Invalid User Account'}, status=400)
            else:
                return JsonResponse({'message': 'An Error Occured Try again later'}, status=400)
    else:
        return render(request, 'login.html')

@csrf_exempt
def signup(request):

    if request.method == "POST":
        data = json.loads(request.body)
        if data:
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            confirm_password = data.get('confirmPassword')
            if password == confirm_password:
                boolean = checkIfUserExists(username=username, email=email)
                if boolean == False:
                    returnValue = createUserAccount(username=username, email=email, password=password)
                    if returnValue == True:
                        return redirect("/login")
                    else:
                        response_data = {'message': 'Failed to create user account'}
                        return JsonResponse(response_data, status=400)
                elif boolean == True:
                    response_data = {'message': 'User account already exists'}
                    return JsonResponse(response_data, status=400)
                else:
                    response_data = {'message': 'An Unknown Error Occured try again later'}
                    return JsonResponse(response_data, status=400)  
            else:
                response_data = {'message': 'Passwords do not match'}
                return JsonResponse(response_data, status=400)

    elif request.method == "GET":
        return render(request, 'signup.html')
    else:
        return HttpResponse("Not Found")
    

def logout(request):    
    authenticated = request.COOKIES.get('authenticated')
    if authenticated == 'true':
        response = JsonResponse({"message": "Logged out successfully"})
        response.delete_cookie("authenticated")
        response.delete_cookie("user")
        return response 
    else:
        pass