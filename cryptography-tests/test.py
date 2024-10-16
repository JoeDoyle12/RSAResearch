from rsa_instance import RSA
from fernet_instance import Fernet

str = b"Hello world!"

rsa_test = RSA()
rsa_encrypted = rsa_test.encrypt(str)
rsa_decrypted = rsa_test.decrypt(rsa_encrypted)


fernet_test = Fernet()
fernet_encrypted = fernet_test.encrypt(str)
fernet_decrypted = fernet_test.decrypt(fernet_encrypted)

print("Original:", str)
print("--------------------")
print("RSA encrypted:", rsa_encrypted)
print("RSA decrypted:", rsa_decrypted)
print("--------------------")
print("Fernet encrypted:", fernet_encrypted)
print("Fernet decrypted:", fernet_decrypted)
