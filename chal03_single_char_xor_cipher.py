import base64
import string
import charfreq
from collections import Counter

inp_dat = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def get_top_x_scores(data, x):
    chars_by_result = {}
    scores_by_result = {}

    for c in string.printable:
        xor_res = [chr(ord(s) ^ ord(c)) for s in base64.b16decode(data, True)]
        xor_res = ''.join(xor_res)

        if(all(d in string.printable for d in xor_res)):
            chars_by_result[xor_res] = c
            scores_by_result[xor_res] = charfreq.cf_eval(xor_res)

    topx = Counter(scores_by_result).most_common(x)
    return [[chars_by_result[val[0]], val[0]] for val in topx]


if __name__ == '__main__':
    num_results = 3
    top = get_top_x_scores(inp_dat, num_results)

    print "most likely keys: "
    for i in range(len(top)):
        print " " + top[i][0] + ": " , top[i][1]
