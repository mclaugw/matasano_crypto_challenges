import binascii
import base64

one = "1c0111001f010100061a024b53535009181c"
two = "686974207468652062756c6c277320657965"

one = int(one, 16)
two = int(two, 16)
res = hex(one ^ two)
print res[2:-1]
