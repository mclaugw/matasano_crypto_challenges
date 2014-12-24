#!/usr/bin/env python

import binascii
import base64

hex_data = '49276d206b696c6c696e6720796f757220627261696e206c' + \
           '696b65206120706f69736f6e6f7573206d757368726f6f6d'
hex_data = hex_data.upper()

print 'hex: ' + hex_data
hex_data = base64.b16decode(hex_data)
hex_data = base64.b64encode(hex_data)
print 'b64: ' + hex_data
hex_data = base64.b64decode(hex_data)
hex_data = base64.b16encode(hex_data)
print 'hex: ' + hex_data
