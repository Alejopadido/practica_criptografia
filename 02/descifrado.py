import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Leyendo el txt para obtener la clave
datos = []
with open("02/keys_output.txt") as fname:
	for lineas in fname:
		datos.append(lineas.split())
# print (datos)

# Clave obtenida de datos[]
clave = bytes.fromhex(datos[15][1])
print(f'Clave de KeyStore: {clave}')

# IV de 0's binarios
iv = bytes.fromhex('00000000000000000000000000000000')
# print(f'iv: {iv}')

# Texto cifrado en b64 a bytes
texto_cifrado_bytes = b64decode('zcFJxR1fzaBj+gVWFRAah1N2wv+G2P01ifrKejICaGpQkPnZMiexn3WXlGYX5WnNIosyKfkNKG9GGSgG1awaZg==')
# print(f'Txt cifrado en bytes: {texto_cifrado_bytes}')

# Desciframos con padding PKCS7
cipher = AES.new(clave, AES.MODE_CBC, iv)
mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size, style="pkcs7")

print(f'Mensaje descifrado en HEX: {mensaje_des_bytes.hex()}')

mensaje_claro = mensaje_des_bytes.decode("utf-8")
print(f'Mensaje descifrado: {mensaje_claro}')


# Descifrado cambiando el padding a x923
# mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size, style="x923")

print(f'Mensaje descifrado en HEX: {mensaje_des_bytes.hex()}')

mensaje_claro = mensaje_des_bytes.decode("utf-8")
print(f'Mensaje descifrado: {mensaje_claro}')


# Visualizando el padding del cifrado (PKCS7)
mensaje_des_bytes = cipher.decrypt(texto_cifrado_bytes)

print(f'Mensaje descifrado en HEX: {mensaje_des_bytes.hex()}')
