#!/usr/bin/env python

import binascii
import base64

hex_data = '49276d206b696c6c696e6720796f757220627261696e206c' + \
           '696b65206120706f69736f6e6f7573206d757368726f6f6d'
known_result = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBs' + \
               'aWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

hex_data = base64.b64encode(base64.b16decode(hex_data, True))

assert hex_data == known_result
