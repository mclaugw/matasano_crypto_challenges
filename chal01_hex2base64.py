import binascii
import base64

data = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print "hex: " + data
data = binascii.a2b_hex(data)
data = base64.b64encode(data)
print "b64: " + data
data = base64.b64decode(data)
data = binascii.b2a_hex(data)
print "hex: " + data
