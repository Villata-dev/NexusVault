from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def derive_key(master_password):
    # Esto transforma tu contraseña en una llave real de cifrado
    password = master_password.encode()
    salt = b'nexus_vault_salt_123' # Sal fija (en el futuro podemos hacerla única)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password))

def encrypt_password(plain_text, master_password):
    key = derive_key(master_password)
    f = Fernet(key)
    return f.encrypt(plain_text.encode()).decode()

def decrypt_password(cipher_text, master_password):
    key = derive_key(master_password)
    f = Fernet(key)
    return f.decrypt(cipher_text.encode()).decode()