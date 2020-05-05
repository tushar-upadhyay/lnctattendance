import os;
from cryptography.fernet import  Fernet

def returnKey():
    return str(os.getenv('fernet_key'))
def getData():
    key = str(os.getenv('fernet_key'))
    print(key)
    key = bytes(key.encode())
    f = Fernet(key)
    t = f.encrypt('tsuhar'.encode())
    print(t)
getData()

