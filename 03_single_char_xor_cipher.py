import base64
import string
import charfreq

data = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
dlen = len(data) / 2
data = int(data, 16)
res2char = {}
res2score = {}
for c in string.printable:
    cstr = int(base64.b16encode(c * dlen), 16)
    xor_res = base64.b16decode(hex(data ^ cstr)[2:-1], True)
    res2char[xor_res] = c
    if(all(d in string.printable for d in xor_res)):
        res2score[xor_res] = charfreq.cf_eval(xor_res)
print "key: ", res2char[max(res2score, key=res2score.get)]
print "result: ", max(res2score, key=res2score.get)
