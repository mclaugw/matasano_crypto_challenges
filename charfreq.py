import string


def cf_eval(str):
    chars = "etaoin"    # 5 most common English characters
    freqs = [0] * 26    # frequency array
    str = str.lower()

    # counting occurences of each letter
    fpos = 0            # position in freq array
    for c in string.lowercase:
        for d in str:
            if c == d:
                freqs[fpos] += 1
        fpos += 1

    score = 1
    fmax = max(freqs)
    for pos in [i for i, j in enumerate(freqs) if j == fmax]:
        for c in chars:
            if pos == string.lowercase.index(c):
                score += 1
    if ' ' in str:
        score += 10
    if '\n' in str or '\r' in str or '\f' in str or '\t' in str:
        score -= 5
    return score
