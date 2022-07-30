# k = k1 ^ k2
# k1 = k ^ k2
# k2 = k ^ k1

def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])


from operator import xor

# Clave del desarrollador (k1)
k1 = bytes.fromhex('A1EF2ABFE1AAEEFF')
print('Clave desarrollador: ',k1.hex())

# Clave del fichero properties (k2)
with open('properties.txt') as f:
    k2 = bytes.fromhex(f.read())
print('Clave Key Manager: ',k2.hex())

# Calculo de clave en memoria (k)
k = xor_data(k1,k2)
print('Clave final: ',k.hex())