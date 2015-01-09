import binascii
import base64
from pprint import pprint
import chal03_single_char_xor_cipher


def hamming(str1, str2):
    assert len(str1) == len(str2)
    bin1 = bin(int(binascii.hexlify(str1), 16))[2:]
    bin2 = bin(int(binascii.hexlify(str2), 16))[2:]
    dist = 0
    for c1, c2 in zip(bin1, bin2):
        if c1 != c2:
            dist += 1
    return dist


def keysize_diff(d, size):
    dist = hamming(d[0:size], d[size:size * 2]) + \
        hamming(d[size * 2:size * 3], d[size * 3:size * 4])
    return [size, dist / (float(size) * 2)]


def chunk(d, size):
    if size < 1:
        size = 1
    return [d[i:i + size] for i in range(0, len(d), size)]


def transpose(chunks):
    transposed = []
    for i in range(0, len(chunks[0])):
        s = ""
        for j in range(0, len(chunks)):
            s += chunks[j][i]
        transposed.append(s)
    return transposed

if __name__ == '__main__':
    with open('chal06_input.txt', 'r') as input_file:
        data = input_file.read().replace('\n', '')
    dists = [keysize_diff(data, i) for i in range(2, 41)]
    keysize = [dists[0][i] for i, j in enumerate(dists) if j == min(dists)]
    data_chunks = chunk(data, keysize[0])
    transposed = transpose(data_chunks)

    for i in range(len(transposed)):
        #print "transposed[i]: " + transposed[i]
        #print "decode: " + base64.b64decode(transposed[i] + "==")
        #print "encode: " + base64.b16encode(base64.b64decode(transposed[i]))
        #print ""
        top = chal03_single_char_xor_cipher.get_top_x_scores(
            base64.b16encode(base64.b64decode(transposed[i])), 3)
        print top
