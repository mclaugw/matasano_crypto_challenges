import string


def cf_eval(in_str):
    chars = "etaoin"    # 5 most common English characters
    freqs = [0] * 26    # frequency array
    in_str = in_str.lower()

    # counting occurences of each letter
    fpos = 0            # position in freq array
    for c in string.lowercase:
        for d in in_str:
            if c == d:
                freqs[fpos] += 1
        fpos += 1

    score = 1
    fmax = max(freqs)
    for pos in [i for i, j in enumerate(freqs) if j == fmax]:
        for c in chars:
            if pos == string.lowercase.index(c):
                score += 10
    if ' ' in in_str:
        score += 5
    if '\n' in in_str or '\r' in in_str or '\f' in in_str or '\t' in in_str:
        score -= 10
    return score
