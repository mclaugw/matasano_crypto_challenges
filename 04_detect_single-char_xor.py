import binascii
import base64
import string
import charfreq


def brute_force(data):
    dlen = len(data) / 2
    data = int(data, 16)
    for c in string.printable:
        cstr = int(base64.b16encode(c * dlen), 16)
        xor_res = data ^ cstr
        xor_res = hex(xor_res)[2:-1]
    #   if len(xor_res) % 16 == 1: # padding
        while len(xor_res) % 16 != 0:
            xor_res = xor_res + '0'
        xor_res = base64.b16decode(xor_res, True)
        #xor_res = base64.b16decode(hex(data ^ cstr)[2:-1], True)
        res2char[xor_res] = c
#       if(all(d in string.printable for d in xor_res)):
        res2score[xor_res] = charfreq.cf_eval(xor_res)
    print 'key: ', res2char[max(res2score, key=res2score.get)]
    print 'score: ', res2score[max(res2score, key=res2score.get)]
    print 'result: ', max(res2score, key=res2score.get)
    best_res = max(res2score, key=res2score.get)
    #print best_res
    best_key = res2char[best_res]
    best_score = res2score[best_res]
    return {'best_key': best_key,
            'best_res': best_res,
            'best_score': best_score}

strings = [line.rstrip('\n') for line in open('gistfile1.txt')]
res2char = {}
res2score = {}

for line in strings:
    if len(line) != 60:
        strings.remove(line)

best_keys = []
best_results = []
best_scores = []

for s in strings:
    temp = brute_force(s)
    best_keys.append(temp['best_key'])
    best_results.append(temp['best_res'])
    best_scores.append(temp['best_score'])

#print 'key: ' + best_keys[max(best_scores)]
#print 'score: ' , best_scores[max(best_scores)]
#print 'res: ' + best_results[max(best_scores)]
#print best_results
