#!/usr/bin/env python

import binascii
import base64
from pprint import pprint
import chal03


def hamming(str1, str2):
    """Calculate and return the hamming distance (bits) between two strings."""
    assert len(str1) == len(str2)
    bin1 = bin(int(binascii.hexlify(str1), 16))[2:]
    bin2 = bin(int(binascii.hexlify(str2), 16))[2:]
    dist = 0
    for c1, c2 in zip(bin1, bin2):
        if c1 != c2:
            dist += 1
    return dist


def avg_dist(d, size):
    """Return the keysize and normalized hamming distance as a list."""
    dist = hamming(d[0:size], d[size:size * 2]) + \
           hamming(d[size * 2:size * 3], d[size * 3:size * 4])
    return [size, dist / (float(size) * 2)]


def chunk(d, size):
    """Split data string into chunks. Return chunks as a list."""
    if size < 1:
        size = 1
    split = [d[i:i + size] for i in range(0, len(d), size)]
    return split


def transpose(chunks):
    """Given an x by y list of chunks, return a y by x list of chunks."""
    transposed = []
    for i in range(0, len(chunks[0])):
        s = ""
        for j in range(0, len(chunks)):
            s += chunks[j][i]
        transposed.append(s)
    return transposed


def b64_2_hex(data):
    """Converts data from hex to base64"""
    return base64.b16encode(base64.b64decode(data))


if __name__ == '__main__':
    with open('chal06_input.txt', 'r') as input_file:
        data = input_file.read().replace('\n', '')
    data = base64.b64decode(data)
    #with open('./definition_of_base64.input', 'r') as input_file:
    #    data = input_file.read().replace('\n', '')
    #data = "RE9PS0lFQlVUVFM="
    #print "b64: ", data
    #print "b64decode: ", base64.b64decode(data)
    #print "b16encode: ", base64.b16encode(base64.b64decode(data))
    #dists = [avg_dist(data, i) for i in range(2, 41)]
    dists = [avg_dist(data, i) for i in range(2, 40)]
    #keysize = [dists[0][i] for i, j in enumerate(dists) if j == min(dists)]
    keysize = [dists[i][0] for i in range(len(dists))]
    data_chunks = chunk(data, keysize[0])
    transposed = transpose(data_chunks)
    transposed = [base64.b64encode(i) for i in transposed]
    transposed = [b64_2_hex(i) for i in transposed]

    for i in range(len(transposed)):
        top = chal03.get_top_x_scores(transposed[i], 10)
        pprint(top)
