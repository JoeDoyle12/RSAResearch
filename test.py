from cryptography_tests.rsa_instance import RSA
from cryptography_tests.fernet_instance import Fernet
import time
import matplotlib.pyplot as plt
from rsa_py.rsa import RSA as HomeRsa

str = ""
with open('test.txt', 'rb') as f:
    str = f.read(128)
tests = 1

rsa_gen, rsa_encrypt, rsa_decrypt = [], [], []
fernet_gen, fernet_encrypt, fernet_decrypt = [], [], []
hrsa_gen, hrsa_encrypt, hrsa_decrypt = [], [], []

hrsa = HomeRsa()

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

    t = time.time()
    hrsa_gen.append(time.time() - t)
    print("Starting HRSA")
    t = time.time()
    hrsa_encrypted = hrsa.encrypt(str)
    hrsa_encrypt.append(time.time() - t)

    t = time.time()
    hrsa_decrypted = hrsa.decrypt(rsa_encrypted)
    hrsa_decrypt.append(time.time() - t)


def avg(list):
    return sum(list) / len(list)

averages = [avg(rsa_gen), avg(rsa_encrypt), avg(rsa_decrypt), avg(fernet_gen), avg(fernet_encrypt), avg(fernet_decrypt)]

fig, axs = plt.subplots(1, 3, figsize=(8, 6))

axs[0].bar([0, 1, 2], [avg(rsa_gen), avg(fernet_gen), avg(hrsa_gen)])
axs[1].bar([0, 1, 2], [avg(rsa_encrypt), avg(fernet_encrypt), avg(hrsa_encrypt)])
axs[2].bar([0, 1, 2], [avg(rsa_decrypt), avg(fernet_decrypt), avg(hrsa_decrypt)])

plt.tight_layout()
plt.show()