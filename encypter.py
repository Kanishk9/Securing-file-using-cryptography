from cryptography.fernet import Fernet

def key_gen():
    key = Fernet.generate_key()
    return key

def encryp(data,key):
    #data = data.encode('utf-8')
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    print("Key is",key.decode())
    print("Encrypted data is",encrypted_data.decode())
    decrypted_data = f.decrypt(encrypted_data)
    print("Decrypted data is",decrypted_data.decode())
    return encrypted_data.decode()