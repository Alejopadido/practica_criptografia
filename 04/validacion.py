import jwt

# ({payload}, key, algorithm)
encoded_jwt = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRmVsaXBlIFJvZHJcdTAwZWRndWV6Iiwicm9sIjoiaXNBZG1pbiJ9.-KiAA8cjkamjwRUiNVHgGeJU8k2wiErdxQP_iFXumM8'

print(encoded_jwt)

decode_jwt = jwt.decode(encoded_jwt,"KeepCoding", algorithms="HS256")

print(decode_jwt)
