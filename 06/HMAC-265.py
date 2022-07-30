from Crypto.Hash import HMAC, SHA256

clave = bytes.fromhex('2712a51c997e14b4df08d55967641b0677ca31e049e672a4b06861aa4d5826eb')

#Generación
msg0= bytes('Siempre existe más de una forma de hacerlo,y más de una solución válida.', 'utf-8')
h = HMAC.new(clave, msg=msg0, digestmod=SHA256)

print(h.hexdigest())
mac = h.hexdigest()

#Verificación
try:
  h.hexverify(mac)
  print("Mensaje validado ok")
except ValueError:
  print("Mensaje validado ko")