"""
test.py: Test Speed of RSA, FErnet, DES, and homemade RSA
Authors: Joe Doyle, Jack Doyle, Aaron Huang
"""

from cryptography_tests.rsa_instance import RSA
from cryptography_tests.fernet_instance import Fernet
import time
import matplotlib.pyplot as plt
from rsa_py.rsa import RSA as HomeRsa
from des_py.des_instance import DES

str = ""
with open('test.txt', 'rb') as f:
    str = f.read()
tests = 10

rsa_gen, rsa_encrypt, rsa_decrypt = [], [], []
fernet_gen, fernet_encrypt, fernet_decrypt = [], [], []
hrsa_gen, hrsa_encrypt, hrsa_decrypt = [], [], []
des_gen, des_encrypt, des_decrypt = [], [], []

for i in range(tests):
    try:
        t = time.time()
        rsa_test = RSA()
        rsa_gen.append(time.time() - t)

        t = time.time()
        rsa_encrypted = rsa_test.encrypt(str)
        rsa_encrypt.append(time.time() - t)

        t = time.time()
        rsa_decrypted = rsa_test.decrypt(rsa_encrypted)
        rsa_decrypt.append(time.time() - t)
    except Exception as e:
        print(f"RSA error on iteration {i}: {e}")

    try:
        t = time.time()
        fernet_test = Fernet()
        fernet_gen.append(time.time() - t)

        t = time.time()
        fernet_encrypted = fernet_test.encrypt(str)
        fernet_encrypt.append(time.time() - t)

        t = time.time()
        fernet_decrypted = fernet_test.decrypt(fernet_encrypted)
        fernet_decrypt.append(time.time() - t)
    except Exception as e:
        print(f"Fernet error on iteration {i}: {e}")

    try:
        t = time.time()
        hrsa = HomeRsa()
        hrsa_gen.append(time.time() - t)

        t = time.time()
        hrsa_encrypted = hrsa.encrypt(str)
        hrsa_encrypt.append(time.time() - t)

        t = time.time()
        hrsa_decrypted = hrsa.decrypt(hrsa_encrypted)
        hrsa_decrypt.append(time.time() - t)
    except Exception as e:
        print(f"HomeRSA error on iteration {i}: {e}")

    try:
        t = time.time()
        des = DES()
        des_gen.append(time.time() - t)

        t = time.time()
        des_encrypted = des.encrypt(str)
        des_encrypt.append(time.time() - t)

        t = time.time()
        des_decrypted = des.decrypt(des_encrypted)
        des_decrypt.append(time.time() - t)
    except Exception as e:
        print(f"DES error on iteration {i}: {e}")


def avg(lst):
    return sum(lst) / len(lst) if lst else 0

# Separate data for RSA + Fernet and HomeRSA + DES
rsa_fernet_types = ['RSA', 'Fernet', 'Total']
homersa_des_types = ['HomeRSA', 'DES', 'Total']

# Calculate total times for each method
rsa_total = avg(rsa_gen) + avg(rsa_encrypt) + avg(rsa_decrypt)
fernet_total = avg(fernet_gen) + avg(fernet_encrypt) + avg(fernet_decrypt)
hrsa_total = avg(hrsa_gen) + avg(hrsa_encrypt) + avg(hrsa_decrypt)
des_total = avg(des_gen) + avg(des_encrypt) + avg(des_decrypt)

# RSA + Fernet
fig1, axs1 = plt.subplots(1, 4, figsize=(12, 6))

# Key Generation, Encryption, Decryption Times
axs1[0].bar(rsa_fernet_types[:-1], [avg(rsa_gen), avg(fernet_gen)])
axs1[0].set_title('Key Generation Time (RSA + Fernet)')

axs1[1].bar(rsa_fernet_types[:-1], [avg(rsa_encrypt), avg(fernet_encrypt)])
axs1[1].set_title('Encryption Time (RSA + Fernet)')

axs1[2].bar(rsa_fernet_types[:-1], [avg(rsa_decrypt), avg(fernet_decrypt)])
axs1[2].set_title('Decryption Time (RSA + Fernet)')

# Add total time bar for RSA and Fernet
axs1[3].bar(['RSA', 'Fernet'], [rsa_total, fernet_total])
axs1[3].set_title('Total Time (RSA + Fernet)')

for ax in axs1:
    ax.set_ylabel("Time (seconds)")

plt.tight_layout()
plt.show()

# HomeRSA + DES
fig2, axs2 = plt.subplots(1, 4, figsize=(12, 6))

# Key Generation, Encryption, Decryption Times
axs2[0].bar(homersa_des_types[:-1], [avg(hrsa_gen), avg(des_gen)])
axs2[0].set_title('Key Generation Time (HomeRSA + DES)')

axs2[1].bar(homersa_des_types[:-1], [avg(hrsa_encrypt), avg(des_encrypt)])
axs2[1].set_title('Encryption Time (HomeRSA + DES)')

axs2[2].bar(homersa_des_types[:-1], [avg(hrsa_decrypt), avg(des_decrypt)])
axs2[2].set_title('Decryption Time (HomeRSA + DES)')

# Add total time bar for HomeRSA and DES
axs2[3].bar(['HomeRSA', 'DES'], [hrsa_total, des_total])
axs2[3].set_title('Total Time (HomeRSA + DES)')

for ax in axs2:
    ax.set_ylabel("Time (seconds)")

plt.tight_layout()
plt.show()
