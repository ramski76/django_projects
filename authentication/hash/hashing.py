import hashlib

def returnHashValue(value):

    sha256 = hashlib.sha256()
    sha256.update(str(value).encode())
    return sha256.hexdigest()