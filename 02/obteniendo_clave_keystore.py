from __future__ import print_function
import base64, textwrap
import jks
import os
from cryptography import x509
from cryptography.hazmat.primitives.serialization import PublicFormat, Encoding


def print_pem(der_bytes, type):
    print("-----BEGIN %s-----" % type)
    print("\r\n".join(textwrap.wrap(base64.b64encode(der_bytes).decode('ascii'), 64)))
    print("-----END %s-----" % type)
    print(" ")
  

path=os.path.dirname(__file__)
print(path)

keystore=path + "/KeyStorePracticas"
ks = jks.KeyStore.load(keystore, "123456")
# Si cualquiera de las claves almacenadas usa una password diferente a la del keystore, se debe hacer con el siguiente comando
#ks.entries["key1"].decrypt("key_password")


# for alias, sk in ks.secret_keys.items():
#     print("Secret key: %s" % sk.alias)
#     print("  Algorithm: %s" % sk.algorithm)
#     print("  Key size: %d bits" % sk.key_size)
#     print("  Key: %s" % "".join("{:02x}".format(b) for b in bytearray(sk.key)))

with open('02/keys_output.txt','a') as f:
    for alias, sk in ks.secret_keys.items():
        f.write("Secret key: %s" % sk.alias)
        f.write('\n')
        f.write("Algorithm: %s" % sk.algorithm)
        f.write('\n')
        f.write("Key size: %d bits" % sk.key_size)
        f.write('\n')
        f.write("Key: %s" % "".join("{:02x}".format(b) for b in bytearray(sk.key)))
        f.write('\n')
