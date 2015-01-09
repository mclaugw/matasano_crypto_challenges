#!/usr/bin/env python

one = "1c0111001f010100061a024b53535009181c"
two = "686974207468652062756c6c277320657965"
known_result = "746865206b696420646f6e277420706c6179"

one = int(one, 16)
two = int(two, 16)
res = hex(one ^ two)[2:-1]

assert res == known_result
