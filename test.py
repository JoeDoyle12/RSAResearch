from cryptography_tests.rsa_instance import RSA
from cryptography_tests.fernet_instance import Fernet
import time
import matplotlib.pyplot as plt

str = ""
with open('test.txt', 'rb') as f:
    str = f.read(128)
tests = 100

rsa_gen, rsa_encrypt, rsa_decrypt = [], [], []
fernet_gen, fernet_encrypt, fernet_decrypt = [], [], []

for i in range(tests):
    t = time.time()
    rsa_test = RSA()
    rsa_gen.append(time.time() - t)

    t = time.time()
    rsa_encrypted = rsa_test.encrypt(str)
    rsa_encrypt.append(time.time() - t)

    t = time.time()
    rsa_decrypted = rsa_test.decrypt(rsa_encrypted)
    rsa_decrypt.append(time.time() - t)

    t = time.time()
    fernet_test = Fernet()
    fernet_gen.append(time.time() - t)

    t = time.time()
    fernet_encrypted = fernet_test.encrypt(str)
    fernet_encrypt.append(time.time() - t)

    t = time.time()
    fernet_decrypted = fernet_test.decrypt(fernet_encrypted)
    fernet_decrypt.append(time.time() - t)

def avg(list):
    return sum(list) / len(list)

print(rsa_gen, rsa_decrypt)

averages = [avg(rsa_gen), avg(rsa_encrypt), avg(rsa_decrypt), avg(fernet_gen), avg(fernet_encrypt), avg(fernet_decrypt)]

fig, axs = plt.subplots(1, 3, figsize=(8, 6))

axs[0].bar([0, 1], [avg(rsa_gen), avg(fernet_gen)])
axs[1].bar([0, 1], [avg(rsa_encrypt), avg(fernet_encrypt)])
axs[2].bar([0, 1], [avg(rsa_decrypt), avg(fernet_decrypt)])

plt.tight_layout()
plt.show()