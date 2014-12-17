import base64
import string
import charfreq
from collections import Counter

data = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
dlen = len(data) / 2
data = int(data, 16)
chars_by_result = {}   # dict with xor result as key and key as value (lol)
scores_by_result = {}  # dict with xor result as key and score as value

for c in string.printable:
    cstr = int(base64.b16encode(c * dlen), 16)
    xor_res = base64.b16decode(hex(data ^ cstr)[2:-1], True)
    chars_by_result[xor_res] = c

    if(all(d in string.printable for d in xor_res)):
        scores_by_result[xor_res] = charfreq.cf_eval(xor_res)

top3 = Counter(scores_by_result).most_common(3)
print "most likely keys: "
for i in range(3):
    print " " + chars_by_result[top3[i][0]] + ": " + top3[i][0]
