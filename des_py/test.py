from des_instance import DES

des = DES()

encrypted = des.encrypt(b"Hello, World!")
print(encrypted)
decrypted = des.decrypt(encrypted)
print(decrypted)