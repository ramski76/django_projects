import sqlite3, hashlib
from ..hash import hashing
from ..models import UserAccounts


def checkIfUserExists(username, email):

    try:
        boolean = UserAccounts.objects.filter(username=username).exists() or UserAccounts.objects.filter(email=email).exists()
        if boolean == True:
            return True
        else:
            return False
    except (Exception):
        return "Error"


def createUserAccount(username, email, password):

    try:
        hashed = hashing.returnHashValue(value=password)
        user = UserAccounts(username=username, email=email, password=hashed)
        user.save()
        return True
    except (Exception) as e:
        return False
