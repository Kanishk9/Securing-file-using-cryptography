from cryptography.fernet import Fernet

def decryp(data,key):
    key = key.encode('utf-8')
    f = Fernet(key)
    decrypted_data = f.decrypt(data)
    return decrypted_data.decode()