from Crypto.Hash import keccak

mensaje = 'En KeepCoding aprendemos cómo protegernos con criptografía.'

k = keccak.new(digest_bits=256)
k.update(bytes(mensaje,'utf-8'))

print(k.hexdigest())

# 3411df16137dcf332a3aa0cca9107ad448fb330b9f77d617c274ad6840953629