from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes

# Leyendo el txt para obtener la clave
datos = []
with open("02/keys_output.txt") as fname:
	for lineas in fname:
		datos.append(lineas.split())
# print (datos)

# Clave obtenida de datos[]
clave = bytes.fromhex(datos[7][1])
print(f'Clave de KeyStore: {clave.hex()}')

# Mensaje a cifrar
mensaje_bytes = bytes('Este curso es de lo mejor que podemos encontrar en el mercado', 'UTF-8')

# Nonce
nonce_mensaje = bytes('9Yccn/f5nJJh','utf-8')

# Datos para generar el tag con Poly1305
datos_asociados = bytes('Datos de autenticacion', 'utf-8')

# Cifrado con ChaCha20Poly1305
cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
cipher.update(datos_asociados)

texto_cifrado, tag = cipher.encrypt_and_digest(mensaje_bytes)

# Encodeando a base64
texto_cifrado_b64 = b64encode(texto_cifrado).decode()
print(texto_cifrado_b64)