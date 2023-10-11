from ..hash import hashing
from ..models import UserAccounts
import sqlite3

def checkCredentials(username, password):

    try:
        hashvalue = hashing.returnHashValue(value=password)     
        users = UserAccounts.objects.values('username', 'password')
        user_data = [{'username': user['username'], 'password': user['password']} for user in users]
        usernames = [user['username'] for user in user_data]
        passwords = [user['password'] for user in user_data]
        if username in usernames and hashvalue in passwords:
            return True
        else:
            return False
        
    except (Exception):
        return "Error"
    

